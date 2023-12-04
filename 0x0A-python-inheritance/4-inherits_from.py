#!/usr/bin/python3
"""Rectangle Module"""


def inherits_from(obj, a_class):
    """checks if obj is a_class type return True if yes False otherwise"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False) 
