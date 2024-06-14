import torch
import torch.nn as nn
from transformers import ViTModel, ViTConfig

class ViTFinetune(nn.Module):
    def __init__(self, num_classes, frozen=False, unfreeze_last_layer=True):
        super().__init__()
        # Charger le modèle ViT pré-entraîné sur ImageNet-21k
        self.backbone = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k')
        self.backbone.classifier = nn.Identity()
        
        if frozen:
            for param in self.backbone.parameters():
                param.requires_grad = False
            if unfreeze_last_layer:
                for param in self.backbone.layernorm.parameters():
                    param.requires_grad = True
                for param in self.backbone.encoder.layer[-1].parameters():
                    param.requires_grad = True

        self.classifier = nn.Linear(self.backbone.config.hidden_size, num_classes)

    def forward(self, x):
        outputs = self.backbone(x).last_hidden_state
        cls_token = outputs[:, 0, :]
        x = self.classifier(cls_token)
        return x
