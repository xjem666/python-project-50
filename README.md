### Hexlet tests and linter status:
[![Actions Status](https://github.com/xjem666/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/xjem666/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7aecba6690861f26e31f/maintainability)](https://codeclimate.com/github/xjem666/python-project-50/maintainability)


### A package for comparing two json/yaml files
Files can be mixed (ex., one file is json, another one is yaml).
There are three provided outputs:
- **stylish** (set by default)
- **plain**
- **json**
***


### Installation guide
```
git clone https://github.com/xjem666/python-project-50
cd python-project-50
make install
```
***

### Help command
```
gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {json,stylish,plain}, --format {json,stylish,plain}
                        output format (default: stylish)
```
***