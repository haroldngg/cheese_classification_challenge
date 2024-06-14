# Cheese Classification challenge
<<<<<<< HEAD
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
=======
This codebase allows you to jumpstart the INF473V challenge.
The goal of this channel is to create a cheese classifier without any real training data.
You will need to create your own training data from tools such as Stable Diffusion, SD-XL, etc...

## Instalation

Cloning the repo:
```
git clone git@github.com:nicolas-dufour/cheese_classification_challenge.git
cd cheese_classification_challenge
```
Install dependencies:
```
conda create -n cheese_challenge python=3.10
conda activate cheese_challenge
```
### Install requirements:
##### Install Pytorch:
If CUDA>=12.0:
```
pip install torch torchvision
```
If CUDA == 11.8
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 
```
Then install the rest of the requirements
```
pip install -r requirements.txt
```

Download the data from kaggle and copy them in the dataset folder
The data should be organized as follow: ```dataset/val```, ```dataset/test```. then the generated train sets will go to ```dataset/train/your_new_train_set```

## Using this codebase
This codebase is centered around 2 components: generating your training data and training your model.
Both rely on a config management library called hydra. It allow you to have modular code where you can easily swap methods, hparams, etc

### Training

To train your model you can run 

```
python train.py
```

This will save a checkpoint in checkpoints with the name of the experiment you have. Careful, if you use the same exp name it will get overwritten

to change experiment name, you can do

```
python train.py experiment_name=new_experiment_name
```

### Generating datasets
You can generate datasets with the following command

```
python generate.py
```

If you want to create a new dataset generator method, write a method that inherits from `data.dataset_generators.base.DatasetGenerator` and create a new config file in `configs/generate/dataset_generator`.
You can then run

```
python generate.py dataset_generator=your_new_generator
```

### VRAM issues
If you have vram issues either use smaller diffusion models (SD 1.5) or try CPU offloading (much slower). For example for sdxl lightning you can do

```
python generate.py image_generator.use_cpu_offload=true
```

## Create submition
To create a submition file, you can run 
```
python create_submition.py experiment_name="name_of_the_exp_you_want_to_score" model=config_of_the_exp
```

Make sure to specify the name of the checkpoint you want to score and to have the right model config
>>>>>>> a90b4086 (final version)
