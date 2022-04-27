#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):

            up += chr(ord(i) - 32)
        else:
            up += i
        print('{}'.format(up))
