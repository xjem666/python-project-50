#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff between two files')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
    else:
        print('''usage: gendiff [-h] first_file second_file 
        Compares two configuration files and shows a difference.
        positional arguments:
        first_file
        second_file

        optional arguments:
        -h, --help            show this help message and exit''')

if __name__ == '__main__':
    main()
