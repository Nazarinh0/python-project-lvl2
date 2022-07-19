"""Diff formatters"""

from gendiff.formatters import format_json, format_stylish


formatters = {
    'json': format_json.render,
    'stylish': format_stylish.stylish,
}
