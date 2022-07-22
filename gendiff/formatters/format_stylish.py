import json

from gendiff.tree_constants import (
    ADDED, CHANGED, INDENT, NESTED, REMOVED, UNCHANGED)


def stylish(diff, depth=1):
    result = []
    indent = INDENT * depth
    for node_key, node_value in diff.items():
        item_type = node_value.get('type')
        item_value = node_value.get('value')
        if item_type == NESTED:
            result.extend([
                f'{indent}{UNCHANGED} {node_key}: {{',
                stylish(item_value, depth + 2),
                f'{indent + INDENT}}}',
            ])
        elif item_type == CHANGED:
            result.extend([
                f'{indent}{REMOVED} {node_key}: {_get_value(node_value.get("old_value"), depth)}',
                f'{indent}{ADDED} {node_key}: {_get_value(node_value.get("new_value"), depth)}',
            ])
        else:
            result.append('{indent}{state} {key}: {value}'.format(
                indent=indent,
                state=item_type,
                key=node_key,
                value=_get_value(item_value, depth)
            ))
    if depth == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def _get_value(item, depth=1):
    if isinstance(item, dict):
        return _render_array(item, depth)
    if isinstance(item, bool) or item is None:
        return json.dumps(item)
    return item


def _render_array(items, depth):
    result = ['{']
    for key, value in items.items():
        result.extend([
            f'{INDENT * (depth + 3)}{key}: {_get_value(value, depth + 2)}'
        ])
    result.append(f'{INDENT * (depth + 1)}}}')
    return '\n'.join(result)
