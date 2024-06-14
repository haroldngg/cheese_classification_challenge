import wandb
import subprocess

sweep_id = 'diywazlw'

def train():
    subprocess.call(['python', 'train.py'])

# Relancer l'agent avec un nouveau count
wandb.agent(sweep_id, function=train, count=30, entity='haroldng', project='challenge_cheese')
