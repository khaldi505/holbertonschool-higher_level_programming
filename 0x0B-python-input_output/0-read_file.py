#!/usr/bin/python3
"""
a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """ filename is a string containing the filename """
    with open(filename, "r", encoding="utf-8") as My_file:
        for line in My_file:
            print("{}".format(line), end="")
