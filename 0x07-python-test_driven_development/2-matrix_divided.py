#!/usr/bin/python3
"""Divide a matrix.

This module has one function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Matrix divided function.

    Args: matrix(list) and div(number)
    Return: A new matrix.
    """

    error_messages = {
        "type": "matrix must be a matrix (list of lists) of integers/floats",
        "rows_size": "Each row of the matrix must have the same size",
        "div_type": "div must be a number",
        "div_zero": "division by zero",
    }

    # Check matrix is a list of lists
    for row in matrix:
        for num in row:
            if not isinstance(row, list) and not isinstance(num, (int, float)):
                raise TypeError(error_messages["type"])

    # Check rows have the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError(error_messages["rows_size"])

    # Check div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError(error_messages["div_type"])
    if div == 0:
        raise ZeroDivisionError(error_messages["div_zero"])

    # Divide each element in the matrix by div
    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
