#!/usr/bin/python3
""""The base of the class system"""


class Base():
    """The base class for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The id system for the program"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
