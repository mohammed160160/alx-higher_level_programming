#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(0, length):
        cl = str[i]
        value = ord(cl)
        if value > 96 and value < 123:
            value = value - 32
        print("{:c}".format(value), end="")
    print(end="\n")
