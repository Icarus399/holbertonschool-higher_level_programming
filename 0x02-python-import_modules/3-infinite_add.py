#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sumL = 0
    for i in range(1, len(argv)):
        sumL += int(argv[i])
    print("{}".format(sumL))
