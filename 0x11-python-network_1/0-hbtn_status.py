#!/usr/bin/python3
import urllib.request
"""  pulls info from https://alx-intranet.hbtn.io/status  """


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as opener:
        info = opener.read()
        print("Body response:")
        print("\t- type:", type(info))
        print("\t- content:", info)
        print("\t- utf8 content:", info.decode(encoding="utf-8"))
