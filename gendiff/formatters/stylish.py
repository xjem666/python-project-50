from itertools import chain
from typing import Any


STATE = {
    'new': '  + ',
    'removed': '  - ',
    'equal': '    ',
}

REPLACER = ' '
SPACES_COUNT = 4
INDENT = REPLACER * SPACES_COUNT


def stringify_value(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        lines = ['{']
        spaces = INDENT * depth
        for key, current_value in value.items():
            if isinstance(value, dict):
                current_value = stringify_value(current_value, depth + 1)
            line = '{spaces}{indent}{key}: {value}'.format(
                spaces=spaces,
                indent=INDENT,
                key=key,
                value=current_value,
            )
            lines.append(line)
        lines.append('{spaces}}}'.format(spaces=spaces))
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, type(None)):
        return 'null'
    return str(value)


def diff_tree(diff_file: dict):
    """Generate list of strings with highlighted differences.
    Parameters:
        diff_file: dict with differences.
    Returns:
        apply_formatter(difference, formatter):
        output of the resulting difference in the selected format.
    """

    def inner(diff_dict: dict, depth):
        lines = []
        space = INDENT * depth
        for key, diff_val in diff_dict.items():
            status = diff_val.get('status')
            current_value = diff_val.get('value')
            if status == 'inserted':
                lines.append(
                    '{space}{indent}{key}: {inserted_value}'.format(
                        space=space,
                        indent=INDENT,
                        key=key,
                        inserted_value=inner(current_value, depth + 1),
                    ),
                )
            elif status == 'updated':
                lines.append('{space}{flag}{key}: {old_value}'.format(
                    space=space,
                    flag=STATE.get('removed'),
                    key=key,
                    old_value=stringify_value(
                        current_value.get('old'),
                        depth + 1,
                    ),
                ),
                )
                lines.append('{space}{flag}{key}: {new_value}'.format(
                    space=space,
                    flag=STATE.get('new'),
                    key=key,
                    new_value=stringify_value(
                        current_value.get('new'),
                        depth + 1,
                    ),
                ),
                )
            else:
                lines.append('{space}{flag}{key}: {value}'.format(
                    space=space,
                    flag=STATE.get(status),
                    key=key,
                    value=stringify_value(current_value, depth + 1),
                ),
                )
        return '\n'.join(chain('{', lines, [space + '}']))

    return inner(diff_file, depth=0)