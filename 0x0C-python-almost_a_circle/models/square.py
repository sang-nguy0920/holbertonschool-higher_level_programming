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

    def update(self, *args, **kwargs):
        """updates/assigns an arg to each attribute"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
