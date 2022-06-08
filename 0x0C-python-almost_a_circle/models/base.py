#!/usr/bin/python3
""" Module holds Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                MyList = []
                for i in list_objs:
                    MyList.append(i.to_dictionary())
                f.write(Base.to_json_string(MyList))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_c = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_c = cls(1)
        dummy_c.update(**dictionary)
        return (dummy_c)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        object_list = []
        dictlist = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                dictlist = cls.from_json_string(f.read())
                for i in dictlist:
                    object_list.append(cls.create(**i))
        except:
            pass
        return object_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ sterializes in CSV """
        file = "{}.csv".format(cls.__name__)
        with open(file, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                My_List = []
                for i in list_objs:
                    My_List.append(i.to_dictionary())
                file.write(cls.to_json_string(My_List))

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in csv """
        mylist = []
        empty = []
        file = "{}.csv".format(cls.__name__)
        with open(file, 'r') as file:
            mylist = cls.from_json_string(file.read())
        for i in mylist:
            empty.append(cls.create(**i))
        return empty
