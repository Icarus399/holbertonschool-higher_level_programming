#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    Dlist = dir(hidden_4)
    for i in range(0, len(Dlist)):
        if Dlist[i][1] != "_":
            print("{}".format(Dlist[i]))
