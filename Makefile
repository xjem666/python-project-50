install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff -h
