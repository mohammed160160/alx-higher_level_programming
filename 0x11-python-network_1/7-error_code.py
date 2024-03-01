#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    REQUEST = requests.get(sys.argv[1])
    if REQUEST.status_code >= 400:
        print("Error code: {}".format(REQUEST.status_code))
    else:
        print(REQUEST.text)
