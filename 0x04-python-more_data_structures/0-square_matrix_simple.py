#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print(matrix)

    listnum = len(matrix)
    listelement = len(matrix[0])
     
    print("======{:d} listnum".format(listnum))
    print("======{:d} listelement".format(listelement))

    mat = [[None] * listelement] * listnum

    print(mat)

    for i in range(0, listnum):

        for j in range(0, listelement):
            mat[i][j]
            print(mat)
            print("======{:d} i {:d} j========".format(i, j))

            mat[i][j] = (mat[i][j]) ** 2
    return (mat)
