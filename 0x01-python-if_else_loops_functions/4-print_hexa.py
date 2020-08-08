#!/usr/bin/python3
string = "{} = {}"
for i in range(0, 99):
    print(string.format(i, hex(i)))
