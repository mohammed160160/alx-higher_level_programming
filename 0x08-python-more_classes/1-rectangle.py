#!/usr/bin/python3
"""Rectangle Module with length and width"""


class Rectangle():
    """This is a Rectangle with 2 integers representing length and width"""
    def __init__(self, width=0, height=0):
        """A starting construction of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets the width as a private attribute"""
        return (self.__width)

    @property
    def height(self):
        """Sets the height as a private attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """To check that height is an int value that is not less than 0
        if not raise error"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        """To check that width is an int value that is not less than 0
        if not raise error"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__width = value
