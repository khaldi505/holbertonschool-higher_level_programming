#!/usr/bin/python3

"""
creating a Square class with the private size attribute
size must be an int and greater than 0
"""


class Square:

    def __init__(self, size=0):
        try:
            if (size < 0):
                raise ValueError("size must be >= 0")
            if (type(size) != int):
                raise TypeError
            elif type(size) == int and size >= 0:
                self._Square__size = size
        except TypeError:
            raise Exception("size must be an integer")
