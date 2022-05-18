#!/usr/bin/python3
""" module containing sqaure"""


class Square:
    """ Defined Square """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if (type(value) != int):
            raise TypeError("size must be int")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
