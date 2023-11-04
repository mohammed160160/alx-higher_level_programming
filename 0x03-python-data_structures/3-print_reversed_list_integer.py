#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    list.reverse(my_list)
    for i in range(0, length):
        print("{:d}".format(my_list[i]))
