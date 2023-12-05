#!/usr/bin/python3
"""save_to_json_file"""

import json


def class_to_json(obj):
    """Return the dictionary represntation of json for the object"""
    return (obj.__dict__)
