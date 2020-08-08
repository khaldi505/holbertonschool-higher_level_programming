#!/usr/bin/python3
"""
print square module
prints a square with the character #.
size is the size length of the square
"""


def print_square(size):
    """print square function"""
    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        elif isinstance(size, float) and size > 0:
            size = int(size)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()
