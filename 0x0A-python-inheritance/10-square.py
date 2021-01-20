#!/usr/bin/python3
"""Module for BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """inits object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                       self.__height)


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """inits object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
