#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    printing = importlib.import_module('hidden_4')
    number = dir(printing)
    length = len(number)
    for i in range(0, length):
        if not number[i].startswith("__"):
            print(number[i])
