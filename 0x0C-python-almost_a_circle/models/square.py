#!/usr/bin/python3
"""Square class module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inits square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size of Square class"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of Square class"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns string rep of rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
