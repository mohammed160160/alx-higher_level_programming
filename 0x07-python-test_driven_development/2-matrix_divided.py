#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not(isinstance(div, int)) and not(isinstance(div, float))):
        raise TypeError('div must be a number')
    if div == 0:
        raise TypeError('division by zero')
    
    listnumber = len(matrix)
    for i in range(0, listnumber):
        listelements = len(matrix[i])
        

        for j in range(0, listelements):
            
        print(end='\n')
