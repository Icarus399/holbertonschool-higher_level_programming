#!/usr/bin/python3
''' add arguments to a python list and then saves tem to a 
    file'''

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

pythonlist = []
jasonfile = "add_item.json"


try:
    pythonlist = load_from_json_file(jasonfile)
except:
    pass
for a in range(1, len(argv)):
    pythonlist.append(argv[a])

save_to_json_file(pythonlist, jasonfile)
