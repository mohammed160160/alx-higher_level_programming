#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]
    tuple_elements = (first_element, second_element)
    return (tuple_elements)
