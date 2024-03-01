#!/usr/bin/python3
import urllib.request

"""pulls info from https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as I:
        info = I.read()
    print("Body response:")
    print("\t- type: {}".format(type(info)))
    print("\t- content: {}".format(info))
    print("\t- utf8 content: {}".format(info.decode(encoding="utf-8")))
