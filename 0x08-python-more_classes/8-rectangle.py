#!/usr/bin/python3
""" Module with the class """


class Rectangle:
    """ defining recatangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Docstring of __init___ method
        Args:
            width (int): size from main to be displayed
            height (int): size from main to be displayed
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
        type(self).print_symbol = self.print_symbol
        """ int: Docstring *after* attribute, with type specified """

    @property
    def width(self):
        """ width """
        return self.__width
        """ width attribute with value """

    @width.setter
    def width(self, value):
        """ Docstring of width
        Args:
            value (int): contains size from __width attribute
        """
        if type(value) != int:
            raise TypeError("width must be int")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        """ width """

    @property
    def height(self):
        """ Docstring height """
        return self.__height
        """  height attribute with value """

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
        """ set height """

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

    def __str__(self):
        if self.area == 0:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[0:-1]

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1
