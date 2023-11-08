#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    top = 0
    bottom = 0
    for group in my_list:
        top += group[0] * group[1]
        bottom += group[1]
    return (top / bottom)
