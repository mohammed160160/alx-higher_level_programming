#!/usr/bin/python3
""""The base of the class system"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class for this project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def height(self):
        """Sets the height as a private attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """To set the value of the heights"""
        self.__height = value

    @property
    def width(self):
        """Sets the width as a private attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """To set the value of the heights"""
        self.__width = value

    @property
    def x(self):
        """Sets the height as a private attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """To set the value of the heights"""
        self.__x = value

    @property
    def y(self):
        """Sets the height as a private attribute"""
        return (self.__y)

    @height.setter
    def y(self, value):
        """To set the value of the heights"""
        self.__y = value
