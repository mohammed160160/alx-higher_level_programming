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

    def to_json(self):
        """Return the dictionary represntation of json for the student class"""
        return (self.__dict__)
