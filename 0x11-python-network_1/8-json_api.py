#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        Argument = sys.argv[1]
    else:
        Argument = ""

    VarQ = {'q': Argument}
    REQUEST = requests.post(url, VarQ)

    try:
        JASON = REQUEST.json()
        if JASON:
            print("[{}] {}".format(JASON['id'], JASON['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
