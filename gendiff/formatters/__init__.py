"""Diff formatters"""

from gendiff.formatters import format_json, format_stylish, format_plain


formatters = {
    'json': format_json.render,
    'stylish': format_stylish.stylish,
    'plain': format_plain.plain
}
