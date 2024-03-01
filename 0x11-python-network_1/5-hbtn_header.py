#!/usr/bin/python3
"""takes and requests from a URL displaying value of X-Reader"""
import requests
import sys

if __name__ == "__main__":
    REQUEST = requests.get(sys.argv[1])
    print(REQUEST.headers.get('X-Request-Id'))
