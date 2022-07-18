import os
from gendiff.parser import parser

def generate_diff(file1, file2):
    first, second = read_file(file1), read_file(file2)
    diff = {}

    for key in first:
        if key in second:
            if first[key] == second[key]:
                diff['  {}'.format(key)] = first[key]
            else:
                diff['- {}'.format(key)] = first[key]
                diff['+ {}'.format(key)] = second[key]
        else:
            diff['- {}'.format(key)] = first[key]

    for key in second:
        if key not in first:
            diff['+ {}'.format(key)] = second[key]

    print_diff(diff)
    return diff


def read_file(file):
    """Read file and return dictionary."""
    with open(file, 'r', encoding='utf-8') as source:
        file_type = os.path.splitext(file)[-1]
        file_data = source.read()
        return parser(file_data, file_type)


def print_diff(diff_data):
    """Print difference."""
    print('{')
    for item_key, item_value in diff_data.items():
        if item_value is True:
            item_value = 'true'
        if item_value is False:
            item_value = 'false'
        print('  {key}: {value}'.format(key=item_key, value=item_value))
    print('}')
