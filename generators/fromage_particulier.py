import torch
from diffusers import (
    DiffusionPipeline,
    EulerDiscreteScheduler,
)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
# with open("~/Desktop/MODAL/token_HF", 'r') as file:
#             token = file.readline()
#########################################################
token = # Put your access token to the repository here !
#########################################################

class Fromage_particulier:
    def __init__(
        self,
        nom_fromage_modele,
        use_cpu_offload=False,
    ):
        base = "stabilityai/stable-diffusion-xl-base-1.0"
        repo = f"ngoupeyoukheng/{nom_fromage_modele}"


        self.pipe = DiffusionPipeline.from_pretrained(
            base, torch_dtype=torch.float16, variant="fp16",
        ).to(device)

        self.pipe.load_lora_weights(repo, token=token)

        self.pipe.scheduler = EulerDiscreteScheduler.from_config(
            self.pipe.scheduler.config, timestep_spacing="trailing"
        )
        self.pipe.set_progress_bar_config(disable=True)


        if use_cpu_offload:
            self.pipe.enable_sequential_cpu_offload()
        self.num_inference_steps = 50
        self.guidance_scale = 0

    def generate(self, prompts):
        images = self.pipe(
            prompts,
            num_inference_steps=self.num_inference_steps,
            guidance_scale=self.guidance_scale,
        ).images
        return images


