#!/usr/bin/python3
def no_c(my_string):
    string_cx = ""
    for char in my_string:
        if char != 67 or char != 99:
            string_cx += char
    return(string_cx)
