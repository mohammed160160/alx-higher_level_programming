#!/usr/bin/python3
"""A module to pulls info from https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as I:
        info = I.read()
    print("Body response:")
    print("\t- type: {}".format(type(info)))
    print("\t- content: {}".format(info))
    print("\t- utf8 content: {}".format(info.decode(encoding="utf-8")))
