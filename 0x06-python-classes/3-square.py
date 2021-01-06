#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Define size of the square"""
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """returns current square area"""
        return self.__size**2
