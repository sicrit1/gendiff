import json
import os
import yaml


YAML_FORMAT = '.yaml'
YML_FORMAT = '.yml'
JSON_FORMAT = '.json'
ERROR = 'Wrong format. Gendiff work with .yaml, .yml, .json file'


def load_data(file_path):
    format_file = check_format(file_path)
    if format_file == JSON_FORMAT:
        with open(file_path) as f:
            data_file = json.load(f)
        return data_file
    elif format_file == YAML_FORMAT:
        with open(file_path) as f:
            data_file = yaml.safe_load(f)
        return data_file
    else:
        raise ERROR


def check_format(file_path):
    filename, file_extension = os.path.splitext(file_path)
    if file_extension == YAML_FORMAT or file_extension == YML_FORMAT:
        return YAML_FORMAT
    elif file_extension == JSON_FORMAT:
        return JSON_FORMAT
    else:
        raise ERROR
