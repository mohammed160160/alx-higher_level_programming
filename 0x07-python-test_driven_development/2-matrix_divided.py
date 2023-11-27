#!/usr/bin/python3
"matrix_divided module"


def matrix_divided(matrix, div):
    """This takes a list of integers and integer/float"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise TypeError('division by zero')

    value = 0
    for i in range(0, len(matrix)):
        if ((i != 0) and (len(matrix[i]) != value)):
            raise TypeError('Each row of the matrix must have the same size')
        value = len(matrix[i])
        for j in range(0, value):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    return ([[round(x / div, 2) for x in row] for row in matrix])
