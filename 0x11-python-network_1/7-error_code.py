#!/usr/bin/python3
''' Python script that tajes in a URL '''

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.content.decode('utf8'))
