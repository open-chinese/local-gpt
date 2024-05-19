import json
from loguru import logger
import pathlib
from os import path


def get_file_path(file_name):
    return path.join(pathlib.Path(__file__).parent.resolve(), file_name)


def load_local_config(config_file):
    config_path = get_file_path(config_file)
    logger.info('[Config] load model_config file: {0}'.format(config_path))
    with open(config_path, 'r', encoding='utf-8') as rf:
        return json.load(rf)


AccessControl = load_local_config('access_control.json')
