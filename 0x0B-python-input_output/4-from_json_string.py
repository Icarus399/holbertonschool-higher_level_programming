#!/usr/bin/python3
""" Module holds function that returns object """
import json


def from_json_string(my_str):
    """ returns object """

    return json.loads(my_str)
