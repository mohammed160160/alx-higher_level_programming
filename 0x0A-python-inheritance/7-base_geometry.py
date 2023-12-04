#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """This is a BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def def integer_validator(self, name, value):
        if not (type(obj) is int):
            raise Exception("area() is not implemented")
