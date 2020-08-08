#!/usr/bin/python3
""" defining the number_of_lines function """


def number_of_lines(filename=""):
    """a function that returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as file_text:
        lineNum = 0
        while True:
            line = file_text.readline()
            if not line:
                break
            else:
                lineNum += 1
    return lineNum
