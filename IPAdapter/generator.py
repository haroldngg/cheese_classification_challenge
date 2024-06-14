import os
import random
import sys
from typing import Sequence, Mapping, Any, Union
import torch


def get_value_at_index(obj: Union[Sequence, Mapping], index: int) -> Any:
    """Returns the value at the given index of a sequence or mapping.

    If the object is a sequence (like list or string), returns the value at the given index.
    If the object is a mapping (like a dictionary), returns the value at the index-th key.

    Some return a dictionary, in these cases, we look for the "results" key

    Args:
        obj (Union[Sequence, Mapping]): The object to retrieve the value from.
        index (int): The index of the value to retrieve.

    Returns:
        Any: The value at the given index.

    Raises:
        IndexError: If the index is out of bounds for the object and the object is not a mapping.
    """
    try:
        return obj[index]
    except KeyError:
        return obj["result"][index]


def find_path(name: str, path: str = None) -> str:
    """
    Recursively looks at parent folders starting from the given path until it finds the given name.
    Returns the path as a Path object if found, or None otherwise.
    """
    # If no path is given, use the current working directory
    if path is None:
        path = os.getcwd()

    # Check if the current directory contains the name
    if name in os.listdir(path):
        path_name = os.path.join(path, name)
        print(f"{name} found: {path_name}")
        return path_name

    # Get the parent directory
    parent_directory = os.path.dirname(path)

    # If the parent directory is the same as the current directory, we've reached the root and stop the search
    if parent_directory == path:
        return None

    # Recursively call the function with the parent directory
    return find_path(name, parent_directory)


def add_comfyui_directory_to_sys_path() -> None:
    """
    Add 'ComfyUI' to the sys.path
    """
    comfyui_path = find_path("ComfyUI")
    if comfyui_path is not None and os.path.isdir(comfyui_path):
        sys.path.append(comfyui_path)
        print(f"'{comfyui_path}' added to sys.path")


def add_extra_model_paths() -> None:
    """
    Parse the optional extra_model_paths.yaml file and add the parsed paths to the sys.path.
    """
    from main import load_extra_path_config

    extra_model_paths = find_path("extra_model_paths.yaml")

    if extra_model_paths is not None:
        load_extra_path_config(extra_model_paths)
    else:
        print("Could not find the extra_model_paths config file.")


add_comfyui_directory_to_sys_path()
add_extra_model_paths()


def import_custom_nodes() -> None:
    """Find all custom nodes in the custom_nodes folder and add those node objects to NODE_CLASS_MAPPINGS

    This function sets up a new asyncio event loop, initializes the PromptServer,
    creates a PromptQueue, and initializes the custom nodes.
    """
    import asyncio
    import execution
    from nodes import init_custom_nodes
    import server

    # Creating a new event loop and setting it as the default loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Creating an instance of PromptServer with the loop
    server_instance = server.PromptServer(loop)
    execution.PromptQueue(server_instance)

    # Initializing custom nodes
    init_custom_nodes()


from nodes import (
    EmptyLatentImage,
    CLIPTextEncode,
    VAEDecode,
    KSampler,
    SaveImage,
    LoadImage,
    NODE_CLASS_MAPPINGS,
    CheckpointLoaderSimple,
)


def main(repo_image, positive_prompt, negative_prompt, name_repo_depo):

    import_custom_nodes()
    with torch.inference_mode():
        checkpointloadersimple = CheckpointLoaderSimple()
        checkpointloadersimple_4 = checkpointloadersimple.load_checkpoint(
            ckpt_name="sd_xl_base_1.0.safetensors"
        )

        emptylatentimage = EmptyLatentImage()
        emptylatentimage_5 = emptylatentimage.generate(
            width=512, height=512, batch_size=5
        )

        cliptextencode = CLIPTextEncode()
        cliptextencode_6 = cliptextencode.encode(
            text=positive_prompt,
            clip=get_value_at_index(checkpointloadersimple_4, 1),
        )

        cliptextencode_7 = cliptextencode.encode(
            text=negative_prompt,
            clip=get_value_at_index(checkpointloadersimple_4, 1),
        )

        ipadapterunifiedloader = NODE_CLASS_MAPPINGS["IPAdapterUnifiedLoader"]()
        ipadapterunifiedloader_10 = ipadapterunifiedloader.load_models(
            preset="PLUS (high strength)",
            model=get_value_at_index(checkpointloadersimple_4, 0),
        )
        for p, filename in enumerate(os.listdir('../input/val_simplified/'+repo_image)):
            loadimage = LoadImage()
            loadimage_21 = loadimage.load_image(image='val_simplified/'+repo_image+'/'+filename)

            ipadapterencoder = NODE_CLASS_MAPPINGS["IPAdapterEncoder"]()
            ipadapterencoder_20 = ipadapterencoder.encode(
                weight=1,
                ipadapter=get_value_at_index(ipadapterunifiedloader_10, 1),
                image=get_value_at_index(loadimage_21, 0),
            )

            ipadapterembeds = NODE_CLASS_MAPPINGS["IPAdapterEmbeds"]()
            ksampler = KSampler()
            vaedecode = VAEDecode()
            saveimage = SaveImage()

            for q in range(1):
                ipadapterembeds_11 = ipadapterembeds.apply_ipadapter(
                    weight=0.7000000000000001,
                    weight_type="linear",
                    start_at=0,
                    end_at=1,
                    embeds_scaling="V only",
                    model=get_value_at_index(ipadapterunifiedloader_10, 0),
                    ipadapter=get_value_at_index(ipadapterunifiedloader_10, 1),
                    pos_embed=get_value_at_index(ipadapterencoder_20, 0),
                    neg_embed=get_value_at_index(ipadapterencoder_20, 1),
                )

                ksampler_3 = ksampler.sample(
                    seed=random.randint(1, 2**64),
                    steps=30,
                    cfg=4,
                    sampler_name="euler",
                    scheduler="karras",
                    denoise=1,
                    model=get_value_at_index(ipadapterembeds_11, 0),
                    positive=get_value_at_index(cliptextencode_6, 0),
                    negative=get_value_at_index(cliptextencode_7, 0),
                    latent_image=get_value_at_index(emptylatentimage_5, 0),
                )

                vaedecode_8 = vaedecode.decode(
                    samples=get_value_at_index(ksampler_3, 0),
                    vae=get_value_at_index(checkpointloadersimple_4, 2),
                )

                saveimage_9 = saveimage.save_images(
                    filename_prefix=name_repo_depo + '_' + str(p) + '_', images=get_value_at_index(vaedecode_8, 0)
                )


