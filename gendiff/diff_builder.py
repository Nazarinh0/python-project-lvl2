from gendiff.tree_constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def build_diff(before, after):
    keys = list(before.keys() | after. keys())
    return {key: generate_node(key, before, after) for key in sorted(keys)}


def generate_node(key, before, after):
    before_value = before.get(key)
    after_value = after.get(key)

    if before_value is None:
        node = {
            'type': ADDED,
            'value': _get(after_value),
        }
    elif after_value is None:
        node = {
            'type': REMOVED,
            'value': _get(before_value),
        }
    elif isinstance(before_value, dict) and isinstance(after_value, dict):
        node = {
            'type': NESTED,
            'value': build_diff(before_value, after_value),
        }
    elif before_value == after_value:
        node = {
            'type': UNCHANGED,
            'value': _get(after_value),
        }
    elif before_value != after_value:
        node = {
            'type': CHANGED,
            'old_value': _get(before_value),
            'new_value': _get(after_value),
        }
    return node


def _get(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
