#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a text file and
    prints it to stdout """

    with open(filename, 'r') as file:
        text = file.read()

    print(text)
