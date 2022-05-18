#!/usr/bin/python3
""" Module containing class square """


class Square:
    """ defined square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
