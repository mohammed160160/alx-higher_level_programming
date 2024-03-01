#!/usr/bin/python3
"""takes and requests from a URL displaying value of X-Reader"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as opener:
        print(opener.headers.get('X-Request-Id'))
