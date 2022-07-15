from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.json import json_format


FORMATS = {
    'plain': plain_format,
    'stylish': stylish_format,
    'json': json_format
}

ERROR = 'Output format {0} is invalid. Chose one of {1}'


def call_formater(item, style='stylish'):
    output_format = FORMATS.get(style)
    if style is not None:
        return output_format(item)
    raise ERROR.format(output_format, list(FORMATS.keys()))
