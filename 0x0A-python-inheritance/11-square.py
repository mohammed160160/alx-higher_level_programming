#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """This is a BaseGeometry"""

    def area(self):
        """Area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is a postive integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is an class that inheret from Base Geometry"""

    def __init__(self, width, height):
        """Creates a rectangle with width and height validated"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the Area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns a representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """This is an class that inheret from Rectangle"""

    def __init__(self, size):
        """Creates a square with size validated"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns a representation of the rectangle"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
