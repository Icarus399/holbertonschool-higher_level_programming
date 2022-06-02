#!/usr/bin/python3
""" Module holds Class """


class Student:
    """ Student class """
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function """
        if attrs is None:
            return self.__dict__
        d = {}
        for i in attrs:
            try:
                d[i] = self.__dict__[i]
            except:
                pass
        return d
