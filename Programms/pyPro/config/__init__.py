import yaml

# load configuration from yml file
def load_config(filename):
    with open(filename, 'r') as ymlfile:
        return yaml.safe_load(ymlfile)

config = load_config('config/config.yml')
