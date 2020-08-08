#!/usr/bin/python3
"""
importing the Base
class module from models
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle is class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        self.__width = width
        return self.__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif type(width) is int:
            if width <= 0:
                raise ValueError("width must be > 0")
        elif type(width) is int and width > 0:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif type(height) is int:
            if height <= 0:
                raise ValueError("height must be > 0")
        elif type(height) is int and height > 0:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not type(x) is int:
            raise TypeError("x must be an integer")
        elif type(x) is int:
            if x < 0:
                raise ValueError("x must be >= 0")
        elif type(x) is int and x > 0:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not type(y) is int:
            raise TypeError("y must be an integer")
        elif type(y) is int:
            if y < 0:
                raise ValueError("y must be >= 0")
        elif type(y) is int and y > 0:
            self.__y = y

    def area(self):
        """" area method returns the rectangle area """
        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for line in range(self.__height):
            for char in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        """ method that returns a string """
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        )
