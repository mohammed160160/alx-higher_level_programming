#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    alength = len(tuple_a)
    blength = len(tuple_b)
    if alength == 0:
        firsta = 0
    else:
        firsta = tuple_a[0]

    if (alength == 0 or alength == 1):
        seconda = 0
    else:
        seconda = tuple_a[1]

    if blength == 0:
        firstb = 0
    else:
        firstb = tuple_b[0]
        
    if (blength == 0 or blength == 1):
        secondb = 0
    else:
        secondb = tuple_b[1]

    first_element = firsta + firstb
    second_element = seconda + secondb
    tuple_elements = (first_element, second_element)
    return (tuple_elements)
