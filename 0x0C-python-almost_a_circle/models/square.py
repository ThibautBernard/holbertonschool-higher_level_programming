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

    def to_dictionary(self):
        """ return the representation of a rectangle with attributs"""
        attrs_to_find = ["id", "size", "x", "y"]
        dict_att = {}
        attributes = [atrb for atrb in dir(self) if not atrb == "__"]
        for i in attributes:
            if i in attrs_to_find:
                dict_att[i] = getattr(self, i)
        return dict_att

    def update(self, *args, **kwargs):
        """ Update attributes """
        attrib = ['id', 'size', 'x', 'y']
        order = [0, 1, 2, 3]
        if args:
            for i in range(len(args)):
                if i > 3:
                    break
                tmp = order.index(i)
                t = attrib[tmp]
                setattr(self, t, args[i])
        else:
            for key, value in kwargs.items():
                if key is not "id" and key in attrib:
                    setattr(self, key, value)
                elif key is "id":
                    if value is None:
                        Base._Base__nb_objects += 1
                        self.id = Base._Base__nb_objects
                    else:
                        setattr(self, key, value)

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
