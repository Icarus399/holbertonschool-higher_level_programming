#!/usr/bin/python3
''' Module holds class Rectangle that inherist from Base '''

from models.base import Base


class Rectangle(Base):
    ''' Rectangle class that inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' class constructor of rectangle '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' returns the area value of our class '''
        return self.width * self.height

    def display(self):
        ''' prints the Rectangle instance '''
        for n in range(self.y):
            print()
        for r in range(self.height):
            for s in range(self.x):
                print(" ", end="")
            for c in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        ''' str function '''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        ''' assigns an argument to each attribute '''
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'width':
                self.width = value
            if key == 'height':
                self.height = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        ''' returns dictionary representation '''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
