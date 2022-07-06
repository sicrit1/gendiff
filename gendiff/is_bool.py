def is_bool(item):
    if type(item) is bool:
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return item
