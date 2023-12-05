#!/usr/bin/python3
"""BaseGeometry Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is an class that inheret from Rectangle"""

    def __init__(self, size):
        """Creates a square with size validated"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)
