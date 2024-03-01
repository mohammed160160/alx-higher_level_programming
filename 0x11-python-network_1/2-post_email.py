#!/usr/bin/python3
"""This is a description"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    REQUEST = urllib.request.Request(URL, EMAIL)

    with urllib.request.urlopen(REQUEST) as Opened:
        Message = Opened.read()
    print(Message.decode('utf-8'))
