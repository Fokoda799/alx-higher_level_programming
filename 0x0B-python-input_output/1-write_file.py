#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write `text to a `file"""

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
