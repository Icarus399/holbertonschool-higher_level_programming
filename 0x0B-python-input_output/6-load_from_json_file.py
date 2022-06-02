#!/usr/bin/python3
""" Module holds function that creates an object """


from asyncore import read
import json


def load_from_json_file(filename):
    """ creates an object from a json file """
    with open(filename) as File:
        return json.loads(File.read())
