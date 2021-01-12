#!/usr/bin/python3
""" Module for a Rectangle """


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area"""
        return (self.__width * self.height)

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            perim = 0
        else:
            perim = self.__width * 2 + self.__height * 2
        return perim

    def __str__(self):
        """returns rectangle with the character #"""
        x = ''
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                x += str('#' * self.__width) + '\n'
        return x[:-1]
