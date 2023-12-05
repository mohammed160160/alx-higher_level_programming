#!/usr/bin/python3
"""This is a program to write a list of list in pyramid"""


def pascal_triangle(n):
    """A function for a triangle"""
    triangle = []

    if n <= 0:
        return (triangle)

    linenum = 0
    triangle.append([1])    
    while len(triangle) != n:
        line = [1]
        lastline = triangle[-1]
        linenum += 1
        for i in range(linenum - 1):
            line.append(lastline[i] + lastline[i+1])
        line.append(1)
        triangle.append(line)

    return (triangle)
