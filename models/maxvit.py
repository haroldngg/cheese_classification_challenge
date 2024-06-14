import torch
import torch.nn as nn
import timm

class MaxViTFinetune(nn.Module):
    def __init__(self, num_classes, model_name='maxvit_base_tf_224.in1k', pretrained=True, frozen=False):
        super(MaxViTFinetune, self).__init__()
        self.backbone = timm.create_model(model_name, pretrained=pretrained, num_classes=0)
        self.classifier = nn.Linear(self.backbone.num_features, num_classes)
        
        if frozen:
            for param in self.backbone.parameters():
                param.requires_grad = False

    def forward(self, x):
        features = self.backbone(x)
        x = self.classifier(features)
        return x