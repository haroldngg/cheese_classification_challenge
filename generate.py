import torch
import wandb
import hydra
<<<<<<< HEAD
import yaml
from tqdm import tqdm
from model_and_cheese_name import liste_association

def change_config(file_path, parameter, new_value):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    config[parameter] = new_value

    with open(file_path, 'w') as file:
        yaml.dump(config, file)

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

for association in liste_association:

    nom_fromage, nom_element = association.split('/')

    write_file(f'./list_of_single_cheese/{nom_element}.txt', nom_fromage)

    # On change les fichiers de configuration
    # labels_file
    change_config(
        file_path = './configs/generate/config.yaml', 
        parameter = 'labels_file', 
        new_value = '${root_dir}/list_of_single_cheese/' + nom_element + '.txt')
    # model_name
    change_config(
        file_path = './configs/generate/image_generator/fromage_particulier.yaml', 
        parameter = 'nom_fromage_modele', 
        new_value = nom_element)
    

    @hydra.main(config_path="configs/generate", config_name="config")
    def generate(cfg):
        dataset_generator = hydra.utils.instantiate(cfg.dataset_generator)

        with open(cfg.labels_file, "r") as f:
            labels = f.readlines()
            labels = [label.strip() for label in labels]

        dataset_generator.generate(labels)


    if __name__ == "__main__":
        generate()
=======
from tqdm import tqdm


@hydra.main(config_path="configs/generate", config_name="config")
def generate(cfg):
    dataset_generator = hydra.utils.instantiate(cfg.dataset_generator)

    with open(cfg.labels_file, "r") as f:
        labels = f.readlines()
        labels = [label.strip() for label in labels]

    dataset_generator.generate(labels)


if __name__ == "__main__":
    generate()
>>>>>>> a90b4086 (final version)
