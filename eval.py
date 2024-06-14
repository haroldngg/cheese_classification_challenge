import torch
import hydra
from tqdm import tqdm

@hydra.main(config_path="configs/eval", config_name="config")
def evaluate(cfg):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = hydra.utils.instantiate(cfg.model.instance).to(device)
    model.load_state_dict(torch.load(cfg.checkpoint_path))
    model.eval()

    loss_fn = hydra.utils.instantiate(cfg.loss_fn)
    datamodule = hydra.utils.instantiate(cfg.datamodule)
    val_loaders = datamodule.val_dataloader()

    val_metrics = {}
    for val_set_name, val_loader in val_loaders.items():
        model.load_state_dict(torch.load(cfg.checkpoint_path))
        epoch_loss = 0
        epoch_num_correct = 0
        num_samples = 0
        y_true = []
        y_pred = []

        for i, batch in enumerate(tqdm(val_loader)):
            images, labels = batch
            images = images.to(device)
            labels = labels.to(device)

            with torch.no_grad():
                preds = model(images)
            loss = loss_fn(preds, labels)
            y_true.extend(labels.detach().cpu().tolist())
            y_pred.extend(preds.argmax(1).detach().cpu().tolist())
            epoch_loss += loss.detach().cpu().numpy() * len(images)
            epoch_num_correct += (
                (preds.argmax(1) == labels).sum().detach().cpu().numpy()
            )
            num_samples += len(images)
        
        epoch_loss /= num_samples
        epoch_acc = epoch_num_correct / num_samples
        val_metrics[f"{val_set_name}/loss"] = epoch_loss
        val_metrics[f"{val_set_name}/acc"] = epoch_acc
        print(f"Validation Set: {val_set_name} - Loss: {epoch_loss:.4f} - Accuracy: {epoch_acc:.4f}")

if __name__ == "__main__":
    evaluate()