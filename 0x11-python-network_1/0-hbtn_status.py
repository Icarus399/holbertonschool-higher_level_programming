#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as intranet:
    intra = intranet.read()
    print("Body response:")
    print("\t- type: {}".format(type(intra)))
    print("\t- content: {}".format(intra))
    print("\t- utf8 content: {}".format(intra.decode('utf8')))
