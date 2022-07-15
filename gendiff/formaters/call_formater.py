from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain


FORMATS = {
    'plain': plain,
    'stylish': stylish,
}

ERROR = 'Output format {0} is invalid. Chose one of {1}'


def call_formater(item, style='stylish'):
    output_format = FORMATS.get(style)
    if style is not None:
        return output_format(item)
    raise ERROR.format(output_format, list(FORMATS.keys()))
