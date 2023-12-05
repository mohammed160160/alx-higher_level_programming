#!/usr/bin/python3
"""My list Module"""


class MyList(list):
    """This is a class to print a list sorted"""

    def print_sorted(self):
        """prints a list of int in order from big to small"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
