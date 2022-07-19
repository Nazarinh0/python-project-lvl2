from gendiff.tree_constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def build_diff(before, after):
    keys = list(before.keys() | after. keys())
    return {key: generate_node(key, before, after) for key in sorted(keys)}


def generate_node(key, before, after):
    before = before.get(key)
    after = after.get(key)

    if before is None:
        node = {
            'type': ADDED,
            'value': _get(after),
        }
    elif after is None:
        node = {
            'type': REMOVED,
            'value': _get(before),
        }
    elif before == after:
        node = {
            'type': UNCHANGED,
            'value': _get(after),
        }
    elif before != after:
        node = {
            'type': CHANGED,
            'old_value': _get(before),
            'new_value': _get(after),
        }
    elif isinstance(before, dict) and isinstance(after, dict):
        node = {
            'type': NESTED,
            'value': build_diff(before, after),
        }
    return node


def _get(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value
