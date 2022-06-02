#!/usr/bin/python3
""" Module holds function that writes an obj to txt file using json """


import json


def save_to_json_file(my_obj, filename):
    """ writes an obj to txt file using json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
