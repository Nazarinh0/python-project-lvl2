import json

from gendiff import generate_diff

def test_flat_json():
    actual = generate_diff("tests/fixtures/flat_before.json",
                           "tests/fixtures/flat_after.json")
    expected = {
              '  host': 'hexlet.io',
              '- timeout': 50,
              '+ timeout': 20,
              '+ proxy': '123.234.53.22',
              '+ follow': False,
              '+ verbose': True
    }

    assert actual == expected
