import itertools
from gendiff.is_bool import is_bool


STATUS = 'status'
ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
VALUE = 'value'
UPDATED_VALUE = 'updated_value'
ERROR = 'Object has no STATUS'


def get_string(item, replacer='  ', x='+ ', y='- ', z='  '):  # noqa: C901

    def iter_(current_item, depth):
        if not isinstance(current_item, dict):
            return str(current_item)

        deep_indent_size = depth + 1
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        list_string = []
        for key, val in current_item.items():
            if val[STATUS] == REMOVED:
                values = is_bool(val[VALUE])
                list_string.append(f'{deep_indent}{y}{key}: {values}')
            elif val[STATUS] == ADDED:
                values = is_bool(val[VALUE])
                list_string.append(f'{deep_indent}{x}{key}: {values}')
            elif val[STATUS] == UNCHANGED:
                values = is_bool(val[VALUE])
                list_string.append(f'{deep_indent}{z}{key}: {values}')
            elif val[STATUS] == UPDATED:
                value1 = is_bool(val[VALUE])
                value2 = is_bool(val[UPDATED_VALUE])
                list_string.append(f'{deep_indent}{y}{key}: {value1}')
                list_string.append(f'{deep_indent}{x}{key}: {value2}')
            elif val[STATUS] == NESTED:
                list_string.append(
                    f"{deep_indent}{z}{key}: "
                    f"{iter_(val[VALUE], deep_indent_size)}"
                )
            else:
                raise ERROR
        result = itertools.chain('{', list_string, [current_indent + '}'])
        return '\n'.join(result)

    return iter_(item, 0)
