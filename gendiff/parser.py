import json
import yaml
import os

def parser(file_data, file_type):
    """Parse input data into .json format."""
    mapping = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    return mapping[file_type](file_data)


def read_file(file):
    """Read file and return dictionary."""
    with open(file, 'r', encoding='utf-8') as source:
        file_type = os.path.splitext(file)[-1]
        file_data = source.read()
        return parser(file_data, file_type)