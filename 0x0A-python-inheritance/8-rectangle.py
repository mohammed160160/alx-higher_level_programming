#!/usr/bin/python3
"""BaseGeometry Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is an class that inheret from Base Geometry"""

    def __init__(self, width, height):
        """Creates a rectangle with width and height validated"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
