import yaml  # Library to parse YAML files

def load_config(config_path="configs/config.yaml"):
    """
    Function to load configuration from a YAML file.
    - Input: Path to the config.yaml file
    - Output: Dictionary containing configuration settings
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Load configuration and store it as a global variable
config = load_config()