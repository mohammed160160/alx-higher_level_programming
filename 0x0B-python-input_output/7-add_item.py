#!/usr/bin/python3
"""adding an argument to a JSON file"""

import sys


saving = __import__('5-save_to_json_file').save_to_json_file
loading = __import__('6-load_from_json_file').load_from_json_file

try:
    argument = loading("add_item.json")
except FileNotFoundError:
    argument = []

argument.extend(sys.argv[1:])
saving(argument, "add_item.json")
