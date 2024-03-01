#!/usr/bin/python3
"""This is a description"""
import urllib.parse
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    REQUEST = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(REQUEST) as Opened:
            print(Opened.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
