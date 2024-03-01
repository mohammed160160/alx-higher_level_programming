#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    URL = "https://api.github.com/user"
    Checking=(sys.argv[1], sys.argv[2])
    REQUEST = requests.get(URL, auth=Checking)

    if REQUEST.status_code == 200:
        print(REQUEST.json().get('id'))
    else:
        print(None)
