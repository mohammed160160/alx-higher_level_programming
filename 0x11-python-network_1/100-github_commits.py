#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    Repo = sys.argv[1]
    Owner = sys.argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(Owner, Repo)
    REQUEST = requests.get(URL)
