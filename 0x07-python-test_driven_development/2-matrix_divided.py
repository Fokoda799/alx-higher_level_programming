#!/usr/bin/python3
"""Divide a matrix

This module has one function that divides all
elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Matrix divided function
       Args: matrix(list) and div(number)
       Return: A new matrix"""

    m="matrix must be a matrix (list of lists) of integers/floats"
    n="Each row of the matrix must have the same size"

    if not all(isinstance(row, list) and \
    all(isinstance(num, (int, float)) for num in row) \
    for row in matrix):
        raise TypeError(m)

    i = 0
    for row in matrix:
        if len(matrix[i]) !=  len(matrix[i+1]):
            raise TypeError(n)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
