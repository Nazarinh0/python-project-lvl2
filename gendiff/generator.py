from gendiff.diff_builder import build_diff
from gendiff.parser import read_file
from gendiff.formatters import formatters


def generate_diff(file1, file2, output_format=None):
    if not output_format:
        output_format = 'stylish'
    first, second = read_file(file1), read_file(file2)
    diff = build_diff(first, second)
    formatter = formatters.get(output_format)
    if not formatter:
        return 'Unsupported formatter'
    return formatter(diff)
