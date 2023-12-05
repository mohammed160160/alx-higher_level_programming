#!/usr/bin/python3
"""Student to Json"""


class Student():
    """A Class of student containing firstname, lastname
    and age"""

    def __init__(self, first_name, last_name, age):
        """To initalize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represntation of json for the student class
        but if attrs is a list of string return the attributes in list"""
        if type(attrs) is list:
            if ((type(element) is str) for element in attrs):
                return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return (self.__dict__)
