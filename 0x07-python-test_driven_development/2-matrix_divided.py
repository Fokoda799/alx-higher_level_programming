#!/usr/bin/python3
"""Matrix divider module



"""


def matrix_divided(matrix, div):
    """Matrix divider module
    """

    m = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(m)
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(m)
    result = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(round(element / div, 2))
        result.append(result_row)
    return result
