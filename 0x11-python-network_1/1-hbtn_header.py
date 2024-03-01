#!/usr/bin/python3
import urllib.request
import sys
"""This is a description"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as opener:
        print(opener.headers.get('X-Request-Id'))
