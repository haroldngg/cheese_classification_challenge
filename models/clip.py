import torch
import torch.nn as nn
from transformers import CLIPModel

class CLIPFinetune(nn.Module):
    def __init__(self, num_classes, model_name="openai/clip-vit-base-patch32", frozen=False, unfreeze_last_layer=True):
        super().__init__()
        self.clip_model = CLIPModel.from_pretrained(model_name)

        # Remplacer la tête du modèle par une identité
        self.clip_model.vision_model.classifier = nn.Identity()

        if frozen:
            for param in self.clip_model.parameters():
                param.requires_grad = False
            if unfreeze_last_layer:
                if hasattr(self.clip_model.vision_model, 'ln_post'):
                    for param in self.clip_model.vision_model.ln_post.parameters():
                        param.requires_grad = True
                if hasattr(self.clip_model.vision_model.encoder.layers, '-1'):
                    for param in self.clip_model.vision_model.encoder.layers[-1].parameters():
                        param.requires_grad = True

        # Obtenir la dimension des embeddings visuels
        vision_embed_dim = self.clip_model.vision_model.config.hidden_size
        
        # Ajouter une nouvelle tête de classification
        self.classifier = nn.Linear(vision_embed_dim, num_classes)

    def forward(self, x):
        # Extraire les features visuelles
        vision_outputs = self.clip_model.vision_model(pixel_values=x).pooler_output

        # Passer les features dans le classifieur
        logits = self.classifier(vision_outputs)

        return logits
