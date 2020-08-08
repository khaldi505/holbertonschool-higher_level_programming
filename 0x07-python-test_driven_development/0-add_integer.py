#!/usr/bin/python3
""" adds two integers
b = (int or float)
a = (int or float)
result = int(a) + int(b)
returns result"""


def add_integer(a, b=98):
    """
    a simple addition function
    """
    result = 0
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    result = (a + b)

    return result
