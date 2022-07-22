import json

from gendiff.tree_constants import (
    ADDED, CHANGED, NESTED, REMOVED, UNCHANGED, COMPLEX)

ADDED_TEXT = "Property '{0}' was added with value: {1}"
REMOVED_TEXT = "Property '{0}' was removed"
CHANGED_TEXT = "Property '{0}' was updated. From {1} to {2}"


def plain(diff, parent=''):
    if not isinstance(diff, dict):
        return str(diff)

    result = []

    for node_key, node_value in diff.items():
        property_value = get_property(parent, node_key)
        node_type = node_value.get('type')

        if node_type == ADDED:
            plain_string = ADDED_TEXT.format(
                property_value,
                get_value(node_value, 'value')
            )
        elif node_type == REMOVED:
            plain_string = REMOVED_TEXT.format(property_value)

        if node_type == NESTED:
            plain_string = plain(node_value.get('value'), property_value)
        elif node_type == CHANGED:
            plain_string = CHANGED_TEXT.format(
                property_value,
                get_value(node_value, 'old_value'),
                get_value(node_value, 'new_value'),
            )
        elif node_type == UNCHANGED:
            continue
        result.append(plain_string)
    return '\n'.join(result)


def get_property(parent, property_name):
    if not parent:
        return property_name
    return f'{parent}.{property_name}'


def get_value(node, value_name):
    value = node.get(value_name)
    if isinstance(value, dict):
        return COMPLEX
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    if isinstance(value, int):
        return value
    return f"'{value}'"
