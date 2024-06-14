# Cheese Classification challenge
The main code comes from the codebase we were given. It uses the same requirements. 

## Confusion Matrix 
The confusion matrix and scores google sheet can be found here : https://docs.google.com/spreadsheets/d/19krb64sv5nCUyPYB_JLUVfQZybjAOdn9nxjGFTFiTPM/edit?usp=sharing 

## Dreambooth 
All the models can be found here : https://huggingface.co/organizations/ngoupeyoukheng/share/XmOOlgcJkZTtanYGHBzvMzRDnXPzZQpWHT 
Warning : The dataset are uncomplete and not the last one. For the dataset, see Final dataset. 

## IP_adapter
There is one additional directory named IPAdapter. 
You wil find there 3 files : the json file coresponding to the IP-adaptor file, and two python files coresponding to the to-python version of our comfyUI architecture. We don't know how much of ComfyUI is required to run those two python files. 
 
If you want to run our IP-Adapter model in ComfyUI : 
  - Install ComfyUI as described : https://github.com/comfyanonymous/ComfyUI 
  - Install the extension for IP-Adapter : https://github.com/cubiq/ComfyUI_IPAdapter_plus 
  - Add the models required (SDXL checkpoint and IP-Adapters checkpoints)
  - If you also want to run the python version of our model, Install the 'comfyUI to python extension : https://github.com/pydn/ComfyUI-to-Python-Extension and put the two python files 'main_generator.py' and 'generator.py' into the ComfyUI_to_python directory. then run main_generator.py. 

## Final dataset
You will find the final dataset in dataset/train/advanced_prompt_advanced_models

## OCR
You will find our OCR codes in the files extract_OCR.py, matches.py and create_submission.py.
