#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = x / y
    except ZeroDivisionError:
        print("Inside result: None")
        return (None)
    finally:
        print("Inside result: {}".format(value))
        return (value)
