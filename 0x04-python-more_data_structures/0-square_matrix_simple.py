#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    listnum = len(matrix)
    listelement = len(matrix[0])

    mat = [[0] * listelement] * listnum

    for i in range(0, listnum):
        for j in range(0, listelement):
            mat[i][j] = matrix[i][j]
            mat[i][j] = (mat[i][j]) ** 2
    return (mat)
