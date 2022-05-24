#!/usr/bin/python3
""" Module with the class """


class Rectangle:
    """ Rectangle Defined"""
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ Docstring of __init___ method
        Args:
            width (int): sizemain to be displayed
            height (int): size main to be displayed
        """
        self.__height = height
        self.__width = width
        """ int: Docstring *after* attribute """

    @property
    def width(self):
        """ Docstring of width """
        return self.__width
        """ returns the w attribute with value """

    @width.setter
    def width(self, value):
        """ Docstring of width
        Args:
            value (int): contains size from __width attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        """ set width """

    @property
    def height(self):
        """ Docstring of height """
        return self.__height
        """ returns the height attribute with value """

    @height.setter
    def height(self, value):
        """ Docstring of height
        Args:
            value (int): contains size from __height attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
        """ height """

    def area(self):
        """ Docstring of area """
        return self.__width * self.__height
        """ height * width """

    def perimeter(self):
        """ Docstring of perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
        """ width * 2 + height * 2 """
