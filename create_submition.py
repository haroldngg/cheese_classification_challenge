import hydra
from torch.utils.data import Dataset, DataLoader
import os
from PIL import Image
import pandas as pd
import torch
import torch.nn.functional as F
from extract_ocr import easyocr_from_path
from matches import identification
import numpy as np
from tqdm import tqdm


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def tensor_to_pil_image(tensor):
    tensor = tensor.cpu().float()
    tensor = tensor / 2 + 0.5  # suppose que le tenseur est normalisé entre -1 et 1
    
    numpy_image = tensor.numpy()
    pil_image = Image.fromarray(numpy_image.transpose(1, 2, 0).astype('uint8'))
    return pil_image

class TestDataset(Dataset):
    def __init__(self, test_dataset_path, test_transform):
        self.test_dataset_path = test_dataset_path
        self.test_transform = test_transform
        images_list = os.listdir(self.test_dataset_path)
        # filter out non-image files
        self.images_list = [image for image in images_list if image.endswith(".jpg")]

    def __getitem__(self, idx):
        image_name = self.images_list[idx]
        image_path = os.path.join(self.test_dataset_path, image_name)
        image = Image.open(image_path)
        image = self.test_transform(image)
        return image, os.path.splitext(image_name)[0]

    def __len__(self):
        return len(self.images_list)


@hydra.main(config_path="configs/train", config_name="config")
def create_submission(cfg):
    test_loader = DataLoader(
        TestDataset(
            cfg.dataset.test_path, hydra.utils.instantiate(cfg.dataset.test_transform)
        ),
        batch_size=1,
        shuffle=False,
        num_workers=cfg.dataset.num_workers,
    )
    # Load model and checkpoint
    model_1 = hydra.utils.instantiate(cfg.model.instance).to(device)
    model_2 = hydra.utils.instantiate(cfg.model.instance).to(device)
    checkpoint_1 = torch.load(cfg.checkpoint_path_1)
    checkpoint_2 = torch.load(cfg.checkpoint_path_2)
    print(f"Loading model from checkpoint: {cfg.checkpoint_path_1}")
    model_1.load_state_dict(checkpoint_1)
    print(f"Loading model from checkpoint: {cfg.checkpoint_path_2}")
    model_2.load_state_dict(checkpoint_2)


    class_names = sorted(os.listdir(cfg.dataset.train_path))

    submission = pd.DataFrame(columns=["id", "label"])
    cheese_classes = [
    "BRIE DE MELUN", "CAMEMBERT", "EPOISSES", "FOURME D'AMBERT", "RACLETTE", "MORBIER", "SAINT-NECTAIRE",
    "POULIGNY SAINT- PIERRE", "ROQUEFORT", "COMTÉ", "CHÈVRE", "PECORINO", "NEUFCHATEL", "CHEDDAR",
    "BÛCHETTE DE CHÈVRE", "PARMESAN", "SAINT- FÉLICIEN", "MONT D’OR", "STILTON", "SCARMOZA", "CABECOU",
    "BEAUFORT", "MUNSTER", "CHABICHOU", "TOMME DE VACHE", "REBLOCHON", "EMMENTAL", "FETA", "OSSAU- IRATY",
    "MIMOLETTE", "MAROILLES", "GRUYÈRE", "MOTHAIS", "VACHERIN", "MOZZARELLA", "TÊTE DE MOINES", "FROMAGE FRAIS"
]

    scores = [
    0.6466784245, 0.642627633, 0.9987515605, 0.299850075, 0.9082652134, 0.7773459189, 0.7266121708,
    0.3198720512, 0.5197920832, 0.7496876302, 0.8995502249, 0.5623242737, 0.8329862557, 0.4997501249,
    0.4997917534, 0.8883953359, 0.5944339368, 0.6920415225, 0.448887982, 0.5452893063, 0.726942299,
    0.6187529748, 0.8328706274, 0.6107717934, 0.5649717514, 0.3331945023, 0.9995654063, 0.4887802711,
    0.5996002665, 0.9994121105, 0.4522732683, 0.6953498479, 0.8995502249, 0.726942299, 0.7642563198,
    0.6661115737, 0.30757401
]

    sorted_cheese_classes = sorted(cheese_classes)

    dico_1 = {sorted_cheese_classes[i]: (0.4455/0.621)*scores[i] for i in range(len(sorted_cheese_classes))}

###modele 0.62 original

    new_scores = [
    0.5944339368, 0.8091385055, 0.9988901221, 0.642627633, 0.8329862557, 0.7140307033, 0.9196321471, 0.5597760896, 0.6535947712, 0.8458285275, 0.9519276535, 0.7996801279, 0.9162848813, 0.6361708573, 0.7132667618, 0.9086778737, 0.7739438891, 0.9561060409, 0.8842752787, 0.7388092134, 0.7854337737, 0.7996001999, 0.9992313605, 0.6870705809, 0.9223674097, 0.5755831566, 0.9995002499, 0.8211353088, 0.7034431692, 0.8567348881, 0.709448565, 0.7996801279, 0.86324398, 0.9126466754, 0.851536468, 0.9983361065, 0.6187529748

]


    ## modele ipadapter
    dico_2 = {sorted_cheese_classes[i]: (0.5266/0.802)*new_scores[i] for i in range(len(sorted_cheese_classes))}
    for i, batch in tqdm(enumerate(test_loader), total=len(test_loader), desc="Making Prediction"):
        images, image_names = batch
        images = images.to(device)
        ######### FAIRE UN SOFT MAX ON VEUT SURTOUT PAS AVOIR UN NOMBRE NEGATIF

        extracted_text = easyocr_from_path('../../../dataset/test/'+image_names[0]+'.jpg') # batch_size = 1
        possible_labels = torch.tensor(identification(extracted_text)).unsqueeze(0).to(device)

       # print((preds*possible_labels)+possible_labels-torch.ones((1,37)).to(device))
        preds_1 = F.softmax(model_1(images), dim=1)
        preds_1 = (preds_1*possible_labels).argmax(1)
        preds_1 = [class_names[pred] for pred in preds_1.cpu().numpy()]

        preds_2 = F.softmax(model_2(images), dim=1)
        preds_2 = (preds_2*possible_labels).argmax(1)
        preds_2 = [class_names[pred] for pred in preds_2.cpu().numpy()]
        


        #print(preds_1, preds_2)

        ############################## DICTIONNAIRES F1 SCORE
        
        ##############################

        if preds_1[0] != preds_2[0]:
            if dico_1[preds_1[0]] >= dico_2[preds_2[0]]:
                final_pred = preds_1[0]
            else:
                final_pred = preds_2[0]
        else:
            final_pred = preds_1[0]
        submission = pd.concat(
            [
                submission,
                pd.DataFrame({"id": image_names, "label": final_pred}),
            ]
        )
    submission.to_csv(f"{cfg.root_dir}/submission.csv", index=False)


if __name__ == "__main__":
    create_submission()
