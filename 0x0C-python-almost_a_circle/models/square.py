#!/usr/bin/python3
""""The base of the class system"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """The Square class for this project"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the square using the same init as a rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a representation of the square in text"""
        sq = ""
        sq += "[Square] ({}) ".format(self.id)
        sq += "{}/{} - {}".format(self.x, self.y, self.width)
        return (sq)

    @property
    def size(self):
        """Sets the width as a private attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """To check and set the value of the width"""
        self.width = value
        self.height = value
