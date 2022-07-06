import json


def load_data(file_path):
    with open(file_path) as f:
        data_file = json.load(f)
    return data_file
