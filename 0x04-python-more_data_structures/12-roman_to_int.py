#!/usr/bin/python3
def roman_to_int(roman_string):
    if ((not roman_string) or not (isinstance(roman_string, str))):
        return 0
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for R in range(0, len(roman_string)):
        if (R > 0 and Roman[roman_string[R]] > Roman[roman_string[R - 1]]):
            number += Roman[roman_string[R]] - (2 * Roman[roman_string[R - 1]])
        else:
            number += Roman[roman_string[R]]
    return (number)
