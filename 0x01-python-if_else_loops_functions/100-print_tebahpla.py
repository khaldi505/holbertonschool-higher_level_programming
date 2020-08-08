#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print("{:s}".format(chr(i)), end='')
    else:
        print("{:s}".format(chr(i - 32)), end='')
