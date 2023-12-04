#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """This is a BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not (type(value) is int):
            raise Exception("{:s} must be an integer".format(name))
        if value <= 0:
            raise Exception("{:s} must be greater than 0".format(name))
