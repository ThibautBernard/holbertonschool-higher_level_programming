#!/usr/bin/python3
"""
    Class Square - that create a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherit from Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Representation of the square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self._size

    @size.setter
    def size(self, value):
        """ size setter """
        if self.integer_validator("width", value):
            self.width = value
            self.height = value
            self._size = value
