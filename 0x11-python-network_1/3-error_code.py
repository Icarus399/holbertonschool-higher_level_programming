#!/usr/bin/python3
''' Python script that takes in a URL, displays the body of the response  '''

from urllib.error import HTTPError
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
