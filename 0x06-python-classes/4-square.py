#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Define size of the square"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returns current square area"""
        return self.__size**2

    @property
    def size(self):
        """size of Square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of Square class"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
