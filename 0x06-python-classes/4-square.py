#!/usr/bin/python3

"""
this new class is based
on the previous task "3-square.py"
we're editing getters and setters
to secure and valditate the user input
"""


class Square:

    def __init__(self, size=0):
        try:
            if (size >= 0) and type(size) == int:
                self._Square__size = size
            if (size < 0):
                raise ValueError("size must be >= 0")
            if not type(size) == int:
                raise TypeError
        except TypeError:
            raise Exception("size must be an integer")

    """ size getter """

    @property
    def size(self):
        return self._Square__size

    """ size setter """

    @size.setter
    def size(self, value):
        try:
            if (value >= 0) and type(value) == int:
                self._Square__size = value
            if (value < 0):
                raise ValueError("size must be >= 0")
            if not type(value) == int:
                raise TypeError
        except TypeError:
            raise Exception("size must be an integer")
        return self._Square__size

    def area(self):
        return self._Square__size * self._Square__size
