#!/usr/bin/python3
''' Python script that takes in a URL '''

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
        print(request.getheader('X-Request-Id'))
