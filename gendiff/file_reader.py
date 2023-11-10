from os.path import splitext


def get_format(filepath: str) -> str:
    _, extension = splitext(filepath)
    if extension in ('.yaml', '.yml'):
        return 'yaml'
    elif extension == '.json':
        return 'json'
    raise TypeError(
        'Check the file(s) extension.\nOnly yaml, yml, or json '
        'file extensions are allowed.'
    )


def read_data(filepath: str):
    with open(filepath) as read_file:
        return read_file.read()