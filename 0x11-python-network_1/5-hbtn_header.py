#!/usr/bin/python3
''' Python script that takes in a URL '''

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    dictionary = res.headers
    print(dictionary.get('X-Request-Id'))
