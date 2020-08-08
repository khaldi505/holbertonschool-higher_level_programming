#!/usr/bin/python3

"""
this new class is based
on the previous task "2-square.py"
we're editing new public methode called area
returns the current square area
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

    def area(self):
        return self._Square__size * self._Square__size
