import yaml

with open('./configs/generate/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

config['labels_file'] = '${root_dir}/list_of_single_cheese/' + 'patato' + '.txt '

with open('./configs/generate/config.yaml', 'w') as file:
    yaml.dump(config, file)