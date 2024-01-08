#!/usr/bin/python3
"""This module is designed to perform the addition of two integers or floats.
Usage:
- Check if this module is not used in another file.
- Import the doctest module to test this code.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args: a & b: The first integer and The second integer
    Returns: The sum of a and b."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile(".tests/0-add_integer.txt")
