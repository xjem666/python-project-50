from gendiff.data_reader import read_data
from gendiff.data_reader import define_extension
from gendiff.data_loader import loader
from gendiff.format_selector import select_formats


def generate_diff(file_path1, file_path2, formatter='stylish'):

    file1 = loader(read_data(file_path1), define_extension(file_path1))
    file2 = loader(read_data(file_path2), define_extension(file_path2))

    formatted_file1 = file1
    formatted_file2 = file2

    return select_formats(formatted_file1, formatted_file2, formatter)
