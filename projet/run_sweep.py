import wandb
import subprocess

sweep_config = {
    'method': 'bayes',
    'metric': {'name': 'real_val/acc', 'goal': 'maximize'},
    'parameters': {
        'epochs': {'min': 5, 'max': 50},
        'lr': {'min': 1e-6, 'max': 1e-3},
        'batch_size' : {'min': 16, 'max': 128}
    }
}

sweep_id = wandb.sweep(sweep=sweep_config, project='challenge_cheese')

def train():
    subprocess.call(['python', 'train.py'])

wandb.agent(sweep_id, function=train, count=20)
