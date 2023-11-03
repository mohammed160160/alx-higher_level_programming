#!/usr/bin/python3
def no_c(my_string):
    string_cx = ""
    for char in my_string:
        if not (char == 'c' or char == 'C'):
            string_cx += char
    return(string_cx)
