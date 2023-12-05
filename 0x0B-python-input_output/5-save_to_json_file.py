#!/usr/bin/python3
"""save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """saves the JSON representation into a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
