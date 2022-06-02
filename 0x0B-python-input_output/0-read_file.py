#!/usr/bin/python3
""" function reads file """


def read_file(filename=""):
    """ reads the file """

    with open(filename) as MyFile:
        print(MyFile.read(), end="")
