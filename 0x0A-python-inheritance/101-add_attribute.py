#!/usr/bin/python3
"""Define a function attributes."""


def add_attribute(obj, att, value):
    """Adds an attribute(att) with (value) to the (object)"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
