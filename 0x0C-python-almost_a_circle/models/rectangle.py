#!/usr/bin/python3
"""Rectangle class module"""


from models.base import Base

class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Inits rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
