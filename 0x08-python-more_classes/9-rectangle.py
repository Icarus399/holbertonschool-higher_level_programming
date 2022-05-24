#!/usr/bin/python3
""" Module """


class Rectangle:
    """ Class defined """
    __width = None
    __height = None
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ init initialized. """
        self.width = width
        self.height = height
        type(self).print_symbol = "#"
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ function to set value to self.__width """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height set """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ element in string """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            for row in range(self.__height):
                for column in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
            return string[:-1]

    def __repr__(self):
        """ represented object """
        string = "Rectangle"
        string += "(" + str(self.width) + "," + str(self.height) + ")"
        return string

    def __del__(self):
        ''' del method '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns new rectangle """
        return cls(size, size)
