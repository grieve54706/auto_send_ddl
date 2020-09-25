import os
from pathlib import Path

import yaml


def get_config():
    base_config = load_config()
    config = dict(base_config)
    return config


def load_config():
    file_name = Path(__file__).parent.parent / 'resource' / 'config.yaml'
    with open(file_name, 'r') as stream:
        return yaml.load(stream, Loader=yaml.CLoader)

