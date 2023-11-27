#!/usr/bin/python3
"matrix_divided module"


def matrix_divided(matrix, div):
    """This takes a list of integers and integer/float"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise TypeError('division by zero')

    for row in matrix:
        if len(row) == 0 or not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    return ([[round(x / div, 2) for x in row] for row in matrix])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
