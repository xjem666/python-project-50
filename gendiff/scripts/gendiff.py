from gendiff import generate_diff
from gendiff.cli import get_arguments


def main():
    diff = generate_diff(*get_arguments())
    print(diff)


if __name__ == '__main__':
    main()
