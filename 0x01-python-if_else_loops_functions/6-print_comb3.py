#!/usr/bin/python3
for num in range(9):
    for numL in range(1, 10):
        if num < numL:
            print("{:d}{:d}".format(num, numL), end="")
            if num != 8 or numL != 9:
                print(", ", end="")
            else:
                print("")
