#!/usr/bin/python3
"""Finds the peak in an unsorted list of integers"""

def find_peak(list_of_integers):
    """This is the function"""

    if len(list_of_integers) == 0:
        return

    leftside = 0
    rightside = len(list_of_integers) - 1

    while leftside < rightside:
        middle = (leftside + rightside) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            leftside = middle +1
        else:
            rightside = middle

    return list_of_integers[leftside]
