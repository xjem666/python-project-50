import json
import argparse


def generate_diff(filepath1, filepath2):
    diff = {}

    with open(filepath1) as file1:
        data1 = json.load(file1)

    with open(filepath2) as file2:
        data2 = json.load(file2)

    for key in data1:
        if key not in data2:
            diff['-' + key] = data1[key]
        elif data1[key] != data2[key]:
            diff['-' + key] = data1[key]
            diff['+' + key] = data2[key]

    for key in data2:
        if key not in data1:
            diff['+' + key] = data2[key]

    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff between two files')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
