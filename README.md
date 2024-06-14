# Cheese Classification challenge
The main code comes from the codebase we were given. It uses the same requirements. 

## IP_adapter
There is one additional directory named IP_Adaptor. 
You wil find there 3 files : the json file coresponding to the IP-adaptor file, and two python files coresponding to the to-python version of our comfyUI architecture. We don't know how much of ComfyUI is required to run those two python files. 
 
If you want to run our IP-Adapter model in ComfyUI : 
  - Install ComfyUI as described : https://github.com/comfyanonymous/ComfyUI 
  - Install the extension for IP-Adapter : https://github.com/cubiq/ComfyUI_IPAdapter_plus 
  - Add the models required (SDXL checkpoint and IP-Adapters checkpoints)
  - If you also want to run the python version of our model, Install the 'comfyUI to python extension : https://github.com/pydn/ComfyUI-to-Python-Extension and put the two python files 'main_generator.py' and 'generator.py' into the ComfyUI_to_python directory. then run main_generator.py. 

