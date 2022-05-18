#!/usr/bin/python3
""" Module conataining the square """


class Square:
    """ defined sqaure """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
             self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if (type(value) == tuple and len(value) == 2 and
            type(value[0]) == int and type(value[1]) is int and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

            raise TypeError("size must be int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.__position[1]):
                print("" * self.__position[1])
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
