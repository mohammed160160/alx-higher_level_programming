#!/usr/bin/python3
"""This is a program to write a list of list in pyramid"""


def pascal_triangle(n):
    """A function for a triangle"""
    triangle = []

    if n <= 0:
        return (triangle)

    linenum = 0

    while len(triangle) != n:
        line = []
        lastline = triangle[linenum - 1]
        linenum += 1
        for i in range(linenum):
            line.append(i+1)
        triangle.append(line)

    return (triangle)
