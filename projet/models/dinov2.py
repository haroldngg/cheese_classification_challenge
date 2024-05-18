import torch
import torch.nn as nn


class DinoV2Finetune(nn.Module):
    def __init__(self, num_classes, frozen=False, unfreeze_last_layer=True, intermediate_state=256):
        super().__init__()
        self.backbone = torch.hub.load("facebookresearch/dinov2", "dinov2_vitb14_reg")
        self.backbone.head = nn.Identity()
        if frozen:
            for param in self.backbone.parameters():
                param.requires_grad = False
            if unfreeze_last_layer:
                for param in self.backbone.norm.parameters():
                    param.requires_grad = True
                for param in self.backbone.blocks[-1].parameters():
                    param.requires_grad = True
        
        # self.classifier_layer_1 = nn.Linear(self.backbone.norm.normalized_shape[0], 256)
        # self.classifier_layer_2 = nn.Linear(256, num_classes)
        self.classifier_layer_2 = nn.Linear(self.backbone.norm.normalized_shape[0], num_classes)

    def forward(self, x):
        x = self.backbone(x)
        # x = nn.LeakyReLU()(self.classifier_layer_1(x))
        # x = nn.Softmax(dim = 1)(self.classifier_layer_2(x))
        x = self.classifier_layer_2(x)

        return x
