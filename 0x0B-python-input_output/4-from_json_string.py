#!/usr/bin/python3
"""from_json_string"""

import json


def from_json_string(my_str):
    """returns the string from JSON representation"""
    return (json.loads(my_str))
