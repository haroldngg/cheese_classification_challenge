
from .base import DatasetGenerator

class AdvancedPromptsDatasetGenerator(DatasetGenerator):
    def __init__(
        self,
        generator,
        batch_size=1,
        output_dir="dataset/train",
        num_images_per_label=200,
    ):
        super().__init__(generator, batch_size, output_dir)
        self.num_images_per_label = num_images_per_label

    def create_prompts(self, labels_names):
        prompts = {}
        for label in labels_names:
            prompts[label] = [
                
                    {"prompt": f"Close-up photo of aged {label} cheese showing detailed texture and color variations, natural lighting, on a wooden cheese board --style raw --v 6.0 --ar 4:3",
                    "num_images": self.num_images_per_label},      
                    
                   { "prompt": f"High-resolution image of fresh {label} cheese with vibrant green basil leaves and olive oil drizzle, bright natural light, white marble background --style raw --v 6.0 --ar 3:2.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Whole {label} cheese wheel on a rustic wooden table, top view, showing the rind and embossed label, early morning sunlight --style raw --v 6.0 --ar 16:9.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Photorealistic image of {label} cheese in its traditional wooden box, open lid, with a soft focus on the creamy texture, evening indoor light --style raw --v 6.0 --ar 3:4.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Photo of sliced {label} cheese hanging in a deli setting, focus on the smooth texture and pale color, natural deli lighting --style raw --v 6.0 --ar 3:2.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Highly detailed photograph of {label} cheese, wrapped in its traditional packaging, with the cheese name clearly printed on the label. The image shows the {label} cheese resting on a light-colored wooden surface, under bright, natural light, emphasizing the colors and textures of both the cheese and its wrapping",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Image of {label} cheese served with black olives and whole grain crackers, top view, on a stone platter, under kitchen lighting --style raw --v 6.0",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Detailed shot of thinly sliced {label} cheese garnished with fresh herbs, focus on the layering and fresh condensation, natural morning light --style raw --v 6.0.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Close-up of a block of {label}cheese on a cold marble surface, emphasizing the clean cuts and natural color of the cheese, bright indoor lighting --style raw --v 6.0.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Image of melted {label} cheese over a slice of rustic toast, close-up to highlight the melting texture and golden color, under warm kitchen lights --style raw --v 6.0.",
                    "num_images": self.num_images_per_label},

                    {"prompt": f"Photo of {label} cheese on a rustic wooden table at a farmhouse, surrounded by countryside elements, early morning light --style raw --v 6.0.",
                    "num_images": self.num_images_per_label},     
                ]
            
        return prompts
