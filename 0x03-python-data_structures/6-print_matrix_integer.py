#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    listnumber = len(matrix)
    for i in range(0, listnumber):
        listelements = len(matrix[i])
        for j in range(0, listelements):
            print("{:d}".format(matrix[i][j]), end='')
            print(end=' ' if j < (listelements - 1) else '')
        print(end='\n')
