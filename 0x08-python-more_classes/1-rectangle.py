#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def height(self):
        return self.height

    def height(self, value):
        if not isinstance(value, int):
            if isinstance(value, float):
                value = int(value)
            else:
                raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def width(self):
        return self.width

    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.value = value
        elif isinstance(value, float):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.value = int(value)
        else:
            raise TypeError("width must be an integer")
