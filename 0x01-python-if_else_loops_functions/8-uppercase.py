#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for x in str:
        if ord(x) > 90:
            new_str += chr(ord(x) - 32)
        else:
            new_str += x
    print('{}'.format(new_str))
