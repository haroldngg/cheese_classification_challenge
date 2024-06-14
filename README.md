# Cheese Classification challenge
Most of the code comes from the codebase we were given. It uses the same requirements. 

## Confusion Matrix 
The confusion matrix and scores can be found on this google sheet : https://docs.google.com/spreadsheets/d/19krb64sv5nCUyPYB_JLUVfQZybjAOdn9nxjGFTFiTPM/edit?usp=sharing 

## Dreambooth 
All the dreambooth models can be found in this huggingface community : https://huggingface.co/organizations/ngoupeyoukheng/share/XmOOlgcJkZTtanYGHBzvMzRDnXPzZQpWHT 
Warning : The dataset on huggingface are uncomplete and not recent. For the dataset, see Final dataset. 

## IP_adapter
There is a directory named IPAdapter. 
You wil find there 3 files : the json file coresponding to the IP-adaptor file, and two python files coresponding to a python script version of the comfyUI architecture. We don't know how much of ComfyUI is required to run those two python files. 
 
If you want to run our IP-Adapter model : 
  - Install ComfyUI as described here : https://github.com/comfyanonymous/ComfyUI 
  - Install the extension for IP-Adapter : https://github.com/cubiq/ComfyUI_IPAdapter_plus 
  - Add the models required (SDXL checkpoint and IP-Adapters checkpoints)
  - If you also want to run the python version of our model, install the 'comfyUI to python' extension : https://github.com/pydn/ComfyUI-to-Python-Extension and put the two python files 'main_generator.py' and 'generator.py' into the ComfyUI_to_python directory. then run main_generator.py. 

## Final dataset
You will find the final dataset in dataset/train/advanced_prompt_advanced_models

## OCR
You will find our OCR codes in the files extract_OCR.py, matches.py and create_submission.py.
