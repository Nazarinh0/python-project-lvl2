### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/python-project-lvl2/actions)
[![Linter check](https://github.com/Nazarinh0/python-project-lvl2/workflows/linter-check/badge.svg)](https://github.com/Nazarinh0/python-project-lvl2/actions/workflows/linter-check.yml)
### Code Climate:
[![Maintainability](https://api.codeclimate.com/v1/badges/2d2d3ddf57e561e5c9c0/maintainability)](https://codeclimate.com/github/Nazarinh0/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d2d3ddf57e561e5c9c0/test_coverage)](https://codeclimate.com/github/Nazarinh0/python-project-lvl2/test_coverage)

Description:

Difference generator - a program that finds the difference between two data structures. This is a popular task, for which there are many online services like http://www.jsondiff.com/. A similar mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Utility features:

- Supported file extensions: yaml, json
- Report available in the form of plain text, stylish and json

Usage example:
[![asciicast](https://asciinema.org/a/512806.svg)](https://asciinema.org/a/512806)



How to install:
- clone repository
- [install poetry](https://python-poetry.org/docs/#installation)
- use `make test`
- use `make build`
- ` pip install dist/hexlet-code-0.1.0.tar.gz`

How to use:
- `gendiff -f[optional] <file_path> <file_path>`
- for more `gendiff -h or --help`
