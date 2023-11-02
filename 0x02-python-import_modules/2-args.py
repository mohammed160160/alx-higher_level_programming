#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    print("{:d} argument".format(count), end="")
    if count != 1:
        print("s", end="")
    print(end=":\n" if count > 0 else ".\n")
    for i in range(0, count):
        j = i + 1
        print("{:d}: {}".format(j, sys.argv[j]))
