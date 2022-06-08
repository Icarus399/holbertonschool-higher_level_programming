#!/usr/bin/python3
""" Module holds class square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """ Str method """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ assings an argument for each attribute """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
