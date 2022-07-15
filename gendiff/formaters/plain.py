STATUS = 'status'
ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UPDATED = 'updated'
VALUE = 'value'
UPDATED_VALUE = 'updated_value'

ADDED_LINE = "Property '{0}' was added with value: {1}"
REMOVED_LINE = "Property '{0}' was removed"
UPDATED_LINE = "Property '{0}' was updated. From {1} to {2}"
COMPLEX = "[complex value]"


def plain_format(item):
    list_plain = []
    for key, val in sorted(flatten(item).items()):
        value = format_value(val[VALUE])
        status_val = val[STATUS]
        if status_val == REMOVED:
            list_plain.append(REMOVED_LINE.format(key))
        elif status_val == ADDED:
            list_plain.append(ADDED_LINE.format(key, value))
        elif status_val == UPDATED:
            updated_value = format_value(val[UPDATED_VALUE])
            list_plain.append(UPDATED_LINE.format(key, value, updated_value))
    return '\n'.join(list_plain)


def flatten(node, prefix='', flatt=None):
    flatted_node = {} if flatt is None else flatt
    for node_key, node_value in node.items():
        new_key = '{0}.{1}'.format(prefix, node_key) if prefix else node_key
        if node_value[STATUS] == NESTED:
            flatten(node_value[VALUE], new_key, flatted_node)
        else:
            flatted_node[new_key] = node_value
    return flatted_node


def format_value(value):
    if isinstance(value, dict):
        return COMPLEX
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'{0}'".format(value)
    return str(value)
