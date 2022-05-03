#!/usr/bin/python3
def no_c(my_string):
    j = ''
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            j += idx
    return j
