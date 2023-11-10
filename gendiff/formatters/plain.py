from typing import Any


def get_plain_format(diff_file, initial_path: str = ''):
    messages = {
        'updated':
            "Property '{path}' was updated. From {old_value} to {new_value}",
        'new':
            "Property '{path}' was added with value: {value}",
        'removed':
            "Property '{path}' was removed",
    }
    diff_text = []
    for key, diff_value in diff_file.items():
        status = diff_value.get('status')
        current_value = diff_value.get('value')
        path = build_path(key, initial_path)
        if status == 'inserted':
            diff_text.append(get_plain_format(current_value, path))
        elif status == 'updated':
            diff_text.append(messages.get(status).format(
                path=path,
                old_value=to_string(current_value.get('old')),
                new_value=to_string(current_value.get('new')),
            ),
            )
        elif status == 'new':
            diff_text.append(messages.get(status).format(
                path=path,
                value=to_string(current_value),
            ),
            )
        elif status == 'removed':
            diff_text.append(messages.get(status).format(
                path=path,
            ),
            )
    return '\n'.join(diff_text)


def build_path(new_point: str, previous_path: str = '') -> str:
    if previous_path:
        return '.'.join([previous_path, new_point])
    return new_point


def to_string(initial_value: Any):
    if isinstance(initial_value, bool):
        return str(initial_value).lower()
    elif isinstance(initial_value, type(None)):
        return 'null'
    elif isinstance(initial_value, dict):
        return '[complex value]'
    elif isinstance(initial_value, str):
        return f"'{initial_value}'"
    return initial_value