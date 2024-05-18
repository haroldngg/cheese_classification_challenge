import torch
import wandb
import hydra
from tqdm import tqdm
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="configs/train", config_name="config", version_base="1.1")
def train(cfg: DictConfig):
    # Convertir la configuration Hydra en un dictionnaire compatible avec wandb
    cfg_dict = OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)
    wandb.init(project="challenge_cheese", name=cfg.experiment_name, config=cfg_dict)
    config = wandb.config
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = hydra.utils.instantiate(cfg.model.instance).to(device)
    optimizer = hydra.utils.instantiate(cfg.optim, params=model.parameters())
    optimizer.param_groups[0]['lr'] = config.lr
    loss_fn = hydra.utils.instantiate(cfg.loss_fn)
    
    # Mettre à jour le datamodule avec le batch_size du sweep
    datamodule = hydra.utils.instantiate(cfg.datamodule, batch_size=config.batch_size)

    train_loader = datamodule.train_dataloader()
    val_loaders = datamodule.val_dataloader()

    for epoch in tqdm(range(config.epochs)):
        epoch_loss = 0
        epoch_num_correct = 0
        num_samples = 0
        for i, batch in enumerate(train_loader):
            images, labels = batch
            images = images.to(device)
            labels = labels.to(device)
            preds = model(images)
            loss = loss_fn(preds, labels)
            wandb.log({"loss": loss.detach().cpu().numpy()})
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.detach().cpu().numpy() * len(images)
            epoch_num_correct += (
                (preds.argmax(1) == labels).sum().detach().cpu().numpy()
            )
            num_samples += len(images)
        epoch_loss /= num_samples
        epoch_acc = epoch_num_correct / num_samples
        wandb.log(
            {
                "epoch": epoch,
                "train_loss_epoch": epoch_loss,
                "train_acc": epoch_acc,
            }
        )
        val_metrics = {}
        for val_set_name, val_loader in val_loaders.items():
            epoch_loss = 0
            epoch_num_correct = 0
            num_samples = 0
            y_true = []
            y_pred = []
            for i, batch in enumerate(val_loader):
                images, labels = batch
                images = images.to(device)
                labels = labels.to(device)
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
            val_metrics[f"{val_set_name}/confusion_matrix"] = (
                wandb.plot.confusion_matrix(
                    y_true=y_true,
                    preds=y_pred,
                    class_names=[
                        datamodule.idx_to_class[i][:10].lower()
                        for i in range(len(datamodule.idx_to_class))
                    ],
                )
            )

        wandb.log(
            {
                "epoch": epoch,
                **val_metrics,
            }
        )
    torch.save(model.state_dict(), cfg.checkpoint_path)

if __name__ == "__main__":
    train()