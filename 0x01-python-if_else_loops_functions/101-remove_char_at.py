#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n > (length - 1) or n < 0:
        print(str)
    else:
        removed = str[:n] + str[-n:]
        print(removed)
