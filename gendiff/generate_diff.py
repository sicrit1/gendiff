# -*- coding:utf-8 -*-


from gendiff.formaters.load_data import load_data
from gendiff.formaters.call_formater import call_formater


STATUS = 'status'
ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
VALUE = 'value'
UPDATED_VALUE = 'updated_value'
ERROR = 'Object has no STATUS'


def calc_diff(dict1, dict2):
    diff = {}
    data_inter = dict1.keys() & dict2.keys()
    data_diff1 = dict1.keys() - dict2.keys()
    data_diff2 = dict2.keys() - dict1.keys()
    for key in data_inter:
        diff[key] = compare(dict1[key], dict2[key])
    for key in data_diff1:
        diff[key] = {STATUS: REMOVED, VALUE: dict1[key]}
    for key in data_diff2:
        diff[key] = {STATUS: ADDED, VALUE: dict2[key]}
    return diff


def compare(item1, item2):
    if isinstance(item1, dict) and isinstance(item2, dict):
        return {STATUS: NESTED, VALUE: calc_diff(item1, item2)}
    if item1 == item2:
        return {STATUS: UNCHANGED, VALUE: item1}
    return {STATUS: UPDATED, VALUE: item1, UPDATED_VALUE: item2}


def generate_diff(file_path1, file_path2, output_format='stylish'):
    file1 = load_data(file_path1)
    file2 = load_data(file_path2)
    diff = calc_diff(file1, file2)
    sorted_diff = sorted_dict(diff)
    return call_formater(sorted_diff, output_format)


def sorted_dict(item):
    if isinstance(item, dict):
        item = dict(sorted(item.items(), key=lambda x: x[0]))
        for k, v in item.items():
            v = sorted_dict(v)
            item[k] = v
        return item
    else:
        return item
