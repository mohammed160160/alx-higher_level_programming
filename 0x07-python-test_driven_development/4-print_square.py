#!/usr/bin/python3
"""Printing a square module"""


def print_square(size):
    """Prints a square based of an argument size"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if size is 0:
        print()
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end='')
            print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
