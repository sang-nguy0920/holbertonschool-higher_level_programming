#!/usr/bin/python3
""" Module for a Rectangle """


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                x += str(str(self.print_symbol) * self.__width) + '\n'
        return x[:-1]

    def __repr__(self):
        """returns string rep of rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """deletes rectangle instance"""
        Rectangle.number_of_instances -= 1
        return print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @staticmethod
    def square(cls, size=0):
        return Rectangle(cls, cls)
