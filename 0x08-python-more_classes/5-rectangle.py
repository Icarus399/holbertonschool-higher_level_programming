
#!/usr/bin/python3
""" Module with the class """


class Rectangle:
    """ Rectangle Defined"""

    def __init__(self, width=0, height=0):
        """ Docstring of __init___ method
        Args:
            width (int): size from main to be displayed
            height (int): size from main to be displayed
        """
        self.__height = height
        self.__width = width
        """ int: Docstring *after* attribute, with type specified """

    @property
    def width(self):
        """ Docstring of width """
        return self.__width
        """ returns the width attribute with value """

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

    @property
    def height(self):
        """  height """
        return self.__height
        """ height attribute with value """

    @height.setter
    def height(self, value):
        """ Docstring of height
        Args:
            value (int): contains size from __height attribute
        """
        if type(value) != int:
            raise TypeError("height must be int")
        if self.__height < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
        """ height """

    def area(self):
        """ Docstring of area """
        return self.__width * self.__height
        """ height * width """

    def perimeter(self):
        """ perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
        """ width * 2 + height * 2 """

    def __str__(self):
        string = ""
        """ Docstring of __str__ method """
        if self.__width != 0 and self.__width != 0:
            string += "\n".join("#" *
                                self.__width for i in range(self.__height))
        return string
        """ string """

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
