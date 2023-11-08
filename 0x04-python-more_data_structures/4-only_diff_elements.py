#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_final = list((set_1 | set_2) - (set_1 & set_2))
    return (set(set_final))
