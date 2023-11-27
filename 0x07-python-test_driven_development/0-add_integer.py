#!/usr/bin/python3
"""add_integer Module"""


def add_integer(a, b=98):
    """This is a module that takes 2 argmuents that adds
    2 integers or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
