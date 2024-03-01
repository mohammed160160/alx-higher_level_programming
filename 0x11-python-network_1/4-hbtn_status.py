#!/usr/bin/python3
"""pulls info from https://alx-intranet.hbtn.io/status using Request"""
import requests

if __name__ == "__main__":
    REQUEST = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(REQUEST)))
    print("\t- content: {}".format(REQUEST))
