import torch
from diffusers import (
    DiffusionPipeline,
    EulerDiscreteScheduler,
)
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file

device = "cuda" if torch.cuda.is_available() else "cpu"

class SDXLBRIEDEMELUNGenerator:
    def __init__(
        self,
        use_cpu_offload=False,
    ):
        base = "stabilityai/stable-diffusion-xl-base-1.0"
        repo = "ngoupeyoukheng/tetedemoines"
       # ckpt = "pytorch_lora_weights.safetensors"

      #  unet = UNet2DConditionModel.from_config(base, subfolder="unet").to(
      #      device, torch.float16
      #  )
       # unet.load_state_dict(load_file(hf_hub_download(repo, ckpt), device=device))
        self.pipe = DiffusionPipeline.from_pretrained(
            base, torch_dtype=torch.float16, variant="fp16",
        ).to(device)
        self.pipe.load_lora_weights("ngoupeyoukheng/tetedemoines")

        self.pipe.scheduler = EulerDiscreteScheduler.from_config(
            self.pipe.scheduler.config, timestep_spacing="trailing"
        )
        self.pipe.set_progress_bar_config(disable=True)
        if use_cpu_offload:
            self.pipe.enable_sequential_cpu_offload()
        self.num_inference_steps = 50
        self.guidance_scale = 12

    def generate(self, prompts):
        images = self.pipe(
            prompts,
            num_inference_steps=self.num_inference_steps,
            guidance_scale=self.guidance_scale,
        ).images
        return images
