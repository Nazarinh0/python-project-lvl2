from gendiff import generate_diff
import tests.expected as expected


def test_flat_json():
    actual = generate_diff("tests/fixtures/flat_before.json",
                           "tests/fixtures/flat_after.json",
                           output_format="stylish")

    assert actual == expected.FLAT_RESULT


def test_nested_json():
    actual = generate_diff("tests/fixtures/nested_before.json",
                           "tests/fixtures/nested_after.json",
                           output_format="stylish")

    assert actual == expected.NESTED_RESULT


def test_json_format():
    actual = generate_diff("tests/fixtures/flat_before.json",
                           "tests/fixtures/flat_after.json",
                           output_format="json")

    assert actual == expected.JSON_FORMAT_RESULT


def test_flat_json_no_format():
    actual = generate_diff("tests/fixtures/flat_before.json",
                           "tests/fixtures/flat_after.json",
                           output_format=None)

    assert actual == expected.FLAT_RESULT


def test_plain_format():
    actual = generate_diff("tests/fixtures/nested_before.json",
                           "tests/fixtures/nested_after.json",
                           output_format="plain")

    assert actual == expected.PLAIN_FORMAT_RESULT
