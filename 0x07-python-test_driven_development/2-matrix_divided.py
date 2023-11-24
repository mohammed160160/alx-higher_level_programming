#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not(isinstance(div, int)) and not(isinstance(div, float))):
        raise TypeError('div must be a number')
    if div == 0:
        raise TypeError('division by zero')
    
    value = 0
    for i in range(0, len(matrix)):
        if ((i != 0) and (len(matrix[i]) != value)):
            raise TypeError('Each row of the matrix must have the same size')
        value = len(matrix[i])
        for j in range(0, value):
            print(matrix[i][j])
            if (not(isinstance(matrix[i][j], int)) and not(isinstance(matrix[i][j], float))):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for i in range(0, len(matrix)):
        for j in range(0, value):
            divided[i][j] = round(divided[i][j] / div, 2)
    return(divided)
