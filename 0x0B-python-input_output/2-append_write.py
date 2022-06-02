#!/usr/bin/python3
""" Module holds function that appends a string """


def append_write(filename="", text=""):
    """ appends a string to a file
        param:
            filename: name of the file
            text: text to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as My_File:
        return My_File.write(text)
