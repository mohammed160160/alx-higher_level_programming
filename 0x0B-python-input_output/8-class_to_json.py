#!/usr/bin/python3
"""save_to_json_file"""


def class_to_json(obj):
    """Return the dictionary represntation of json for the object"""
    return (obj.__dict__)
