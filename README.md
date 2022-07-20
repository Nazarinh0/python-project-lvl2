### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/python-project-lvl2/actions)
### Code Climate:
[![Maintainability](https://api.codeclimate.com/v1/badges/2d2d3ddf57e561e5c9c0/maintainability)](https://codeclimate.com/github/Nazarinh0/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d2d3ddf57e561e5c9c0/test_coverage)](https://codeclimate.com/github/Nazarinh0/python-project-lvl2/test_coverage)

Description:

Difference calculator - a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com/. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility features:

- Support for different input formats: yaml, json
- Report generation in the form of plain text, stylish and json

Usage example:
```python
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```


How to install:
- clone repository
- [install poetry](https://python-poetry.org/docs/#installation)
- use `make test`
- use `make build`
- ` pip install dist/hexlet-code-0.1.0.tar.gz`

How to use:
- `gendiff -f[optional] <file_path> <file_path>`
- for more `gendiff -h or --help`

Use an application to find out the difference in two files with nested or flat structure, format = string, available formats are:
stylish, plain, json
!!ASCIINEMA HERE!!
