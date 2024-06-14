# models/swin.py
import torch
import torch.nn as nn
import timm

class SwinTransformerFinetune(nn.Module):
    def __init__(self, num_classes, frozen=False, unfreeze_last_layer=True):
        super(SwinTransformerFinetune, self).__init__()

        # Charger le modèle Swin Transformer pré-entraîné à partir de timm
        self.backbone = timm.create_model('swin_base_patch4_window7_224', pretrained=True, num_classes=0)  # `num_classes=0` to remove the classifier
        
        if frozen:
            for param in self.backbone.parameters():
                param.requires_grad = False
            if unfreeze_last_layer:
                for param in self.backbone.layers[-1].parameters():
                    param.requires_grad = True

        # Ajouter les couches de classification personnalisées
        self.classifier = nn.Linear(self.backbone.num_features, num_classes)

    def forward(self, x):
        features = self.backbone(x)
        x = self.classifier(features)
        return x
