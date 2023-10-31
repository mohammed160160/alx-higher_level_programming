#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n > (length - 1) or n < 0:
        return(str)
    else:
        removed = str[0:n] + str[n+1:]
        return(removed)
