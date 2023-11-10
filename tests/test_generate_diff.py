import os
import pytest
from gendiff.file_reader import read_data
from gendiff.gendiff import generate_diff
from gendiff.formatters import JSON, STYLISH, PLAIN


def get_answer(answer_path):
    return read_data(answer_path)


def get_fixture_path(file_name):
    return os.path.join('tests', 'fixtures', file_name)


@pytest.mark.parametrize('filepath1, filepath2, format_name, answer', [
    ('file1.json', 'file2.json', STYLISH, 'answer_stylish_flat'),
    ('file1.yaml', 'file2.yaml', STYLISH, 'answer_stylish_flat'),
    ('file1.yml', 'file2.yml', STYLISH, 'answer_stylish_flat'),
    (
            'file1_nested.json', 'file2_nested.json',
            STYLISH, 'answer_stylish_nested'
    ),
    (
            'file1_nested.yaml', 'file2_nested.yaml',
            STYLISH, 'answer_stylish_nested'
    ),
    ('file1.json', 'file2.json', PLAIN, 'answer_plain_flat'),
    ('file1.yaml', 'file2.yaml', PLAIN, 'answer_plain_flat'),
    ('file1.yml', 'file2.yml', PLAIN, 'answer_plain_flat'),
    ('file1_nested.json', 'file2_nested.json', PLAIN, 'answer_plain_nested'),
    ('file1_nested.yaml', 'file2_nested.yaml', PLAIN, 'answer_plain_nested'),
    ('file1.json', 'file2.json', JSON, 'answer_json_flat'),
    ('file1.yaml', 'file2.yaml', JSON, 'answer_json_flat'),
    ('file1.yml', 'file2.yml', JSON, 'answer_json_flat'),
    ('file1_nested.json', 'file2_nested.json', JSON, 'answer_json_nested'),
    ('file1_nested.yaml', 'file2_nested.yaml', JSON, 'answer_json_nested'),
])
def test_generate_diff(filepath1, filepath2, format_name, answer):
    answer = get_answer(get_fixture_path(answer))
    assert generate_diff(
        get_fixture_path(filepath1),
        get_fixture_path(filepath2),
        format_name
    ) == answer
