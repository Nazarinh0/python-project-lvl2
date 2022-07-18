from gendiff.tree_constants import ADDED, CHANGED, INDENT, NESTED, REMOVED, UNCHANGED


def stylish(diff, depth=1):
    result = []
    indent = INDENT * depth
    for key, value in diff.items():