#!/usr/bin/python3
"""Say_my_name module"""


def say_my_name(first_name, last_name=""):
    """A function that takes a string first_name and last_name
    as it's arguments"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
