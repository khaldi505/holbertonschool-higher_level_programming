#!/usr/bin/python3
for c in range(0, 100):
    if c == 89:
        print("{:02d}".format(c))
    elif c % 10 > c / 10:
        print("{:02d}".format(c), end=", ")
