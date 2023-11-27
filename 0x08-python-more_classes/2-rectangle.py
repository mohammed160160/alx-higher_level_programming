#!/usr/bin/python3
"""Rectangle Module with 2d parameters"""


class Rectangle():
    """This is a Rectangle with 2 integers representing length and width"""
    def __init__(self, width=0, height=0):
        """A starting construction of the class"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Sets the height as a private attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """To check that height is an int value that is not less than 0
        if not raise error"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Sets the width as a private attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """To check that width is an int value that is not less than 0
        if not raise error"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """A Construction for the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """A Construction for the parameter of the rectangle"""
        if (self.__width or self.__height) == 0:
            return(0)
        return((self.__width + self.__height) * 2)
