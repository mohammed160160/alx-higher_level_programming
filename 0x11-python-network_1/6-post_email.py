#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    REQUEST = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(REQUEST.text)
