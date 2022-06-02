#!/usr/bin/python3
""" Module holds function that returns JSON """
import json


def to_json_string(my_obj):
    """ returns json representation of object """

    return json.dumps(my_obj)
    print(to_json_string)
