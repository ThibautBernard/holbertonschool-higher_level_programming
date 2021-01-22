#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle that inherit from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """ return the representation of a rectangle with attributs"""
        attrs_to_find = ["width", "height", "x", "y", "id"]
        dict_att = {}
        attributes = [atrb for atrb in dir(self) if not atrb == "__"]
        for i in attributes:
            if i in attrs_to_find:
                dict_att[i] = getattr(self, i)
        return dict_att

    def integer_validator(self, name_attr, value):
        """Check value """
        attr1 = ["width", "height", "size"]
        if type(value) == int:
            if name_attr in attr1:
                if value > 0:
                    return 1
                else:
                    raise ValueError("{} must be > 0".format(name_attr))
            elif name_attr == "y" or name_attr == "x":
                if value >= 0:
                    return 1
                else:
                    raise ValueError("{} must be >= 0".format(name_attr))
        else:
            raise TypeError("{} must be an integer".format(name_attr))

    def update(self, *args, **kwargs):
        """ Update attributes """
        attrib = ['id', 'width', 'height', 'x', 'y']
        order = [0, 1, 2, 3, 4]
        if args:
            for i in range(len(args)):
                if i > 4:
                    break
                tmp = order.index(i)
                t = attrib[tmp]
                if self.integer_validator(t, args[i]) or t == "id":
                    setattr(self, t, args[i])
        else:
            for key, value in kwargs.items():
                if self.integer_validator(key, value) or key == "id":
                    setattr(self, key, value)

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.__width) * (self.__height)

    def display(self):
        """ print rectangle from width and height and x,y """
        if self.y:
            print("\n" * self.y, end="")
        for i in range(0, self.height):
            if self.x:
                print(" " * self.x, end="")
            print("#" * self.width, end="")
            print("")

    def __str__(self):
        """ return rectangle informations"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)

    @property
    def width(self):
        """ Getter width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if self.integer_validator("width", value):
                self.__width = value

    @property
    def height(self):
        """ Getter height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if self.integer_validator("height", value):
            self.__height = value

    @property
    def x(self):
        """ Getter x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter """
        if self.integer_validator("x", value):
            self.__x = value

    @property
    def y(self):
        """ Getter x attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if self.integer_validator("y", value):
                self.__y = value
