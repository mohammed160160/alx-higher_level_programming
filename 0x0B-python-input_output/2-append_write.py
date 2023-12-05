#!/usr/bin/python3
"""Writing into a file"""


def write_file(filename="", text=""):
    """Reading a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
