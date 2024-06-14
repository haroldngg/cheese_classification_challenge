import torch
import hydra
import os

@hydra.main(config_path="configs/eval", config_name="soup")
def create_model_soup(cfg):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model_paths = cfg.model_paths 
    
    if not model_paths:
        raise ValueError("No model paths provided in the configuration.")
    
  
    models = []
    for path in model_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Checkpoint file not found: {path}")
        model = hydra.utils.instantiate(cfg.model.instance).to(device)
        model.load_state_dict(torch.load(path, map_location=device))
        models.append(model)
    
    soup_model = hydra.utils.instantiate(cfg.model.instance).to(device)
    state_dict = models[0].state_dict()
    for key in state_dict.keys():
        state_dict[key] = torch.mean(torch.stack([model.state_dict()[key] for model in models]), dim=0)
    soup_model.load_state_dict(state_dict)
    
    torch.save(soup_model.state_dict(), cfg.soup_checkpoint_path)
    print(f"Sauvegarde du modèle soupe à {cfg.soup_checkpoint_path}")

if __name__ == "__main__":
    create_model_soup()
