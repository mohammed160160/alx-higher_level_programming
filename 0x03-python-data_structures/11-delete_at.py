#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx > (length - 1):
        return (my_list)
    new_list = my_list[:idx] + my_list[(idx + 1):]
    return (new_list) 
