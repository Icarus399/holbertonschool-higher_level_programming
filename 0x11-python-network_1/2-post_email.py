#!/usr/bin/python3
''' Python script that takes in a URL '''

import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    mail = urllib.parse.urlencode({'email': argv[2]})
    mail = mail.encode('utf8')
    with urllib.request.urlopen(url, mail) as res:
        print(res.read().decode('utf8'))
