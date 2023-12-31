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
        """To check and set the value of the height"""
        self.validationcheck("height", value)
        self.__height = value

    @property
    def width(self):
        """Sets the width as a private attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """To check and set the value of the width"""
        self.validationcheck("width", value)
        self.__width = value

    @property
    def x(self):
        """Sets the x as a private attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """To check and set the value of x"""
        self.validationcheck("x", value)
        self.__x = value

    @property
    def y(self):
        """Sets the y as a private attribute"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """To set and check the value of y"""
        self.validationcheck("y", value)
        self.__y = value

    @staticmethod
    def validationcheck(name, value):
        """Checks the validation of each variable in the class"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ("x", "y"):
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Returns the area of the rectangle class"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns a representation of the rectangle in text"""
        Rect = ""
        Rect += "[Rectangle] ({}) ".format(self.id)
        Rect += "{}/{} - ".format(self.__x, self.__y)
        Rect += "{}/{}".format(self.__width, self.__height)
        return (Rect)

    def display(self):
        """Returns a representation of the rectangle in #"""
        rect = ""
        for y in range(self.__y):
            rect += "\n"
        for i in range(self.__height):
            x = 0
            for x in range(self.__x):
                rect += " "
            for j in range(self.__width):
                rect += "#"
            if i is not (self.__height - 1):
                rect += "\n"
        print(rect)

    def update(self, *args, **kwargs):
        """Updates a values of a rectangle class using args and kawargs"""
        if len(args) == 0:
            for string, value in kwargs.items():
                self.__setattr__(string, value)
        else:
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.width = b
                if a == 2:
                    self.height = b
                if a == 3:
                    self.x = b
                if a == 4:
                    self.y = b

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
        return (dic)
