import json
import yaml

def parser(file_data, file_type):
    """Parse input data into .json format."""
    mapping = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    return mapping[file_type](file_data)