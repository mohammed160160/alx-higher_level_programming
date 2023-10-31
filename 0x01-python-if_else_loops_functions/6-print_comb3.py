#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0,10):
        if i != j and i < j:
            print(f"{i}{j}", end="")
            if ((i * 10) + j) != 89:
                print(f", ", end="")
            else:
                print()
