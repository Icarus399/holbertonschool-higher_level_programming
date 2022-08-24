#!/usr/bin/python3
''' Python script that takes in a URL '''

import requests
import sys

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    output = res.content.decode('utf8')
    print(output)
