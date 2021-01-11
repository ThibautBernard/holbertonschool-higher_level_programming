#!/usr/bin/python3
"""
Rectangle class - define a rectangle
"""


class Rectangle:
    """ class rectangle that create a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor function
        Args:
            width: (int): width of Rectangle
            height: (int): heigth of Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = type(self).print_symbol

    def __str__(self):
        """ string representation of the object """
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(0, self.__height):
            for y in range(0, self.__width):
                if not isinstance(self.print_symbol, str):
                    s += str(self.print_symbol)
                else:
                    s += self.print_symbol
            if i + 1 != self.__height:
                s += "\n"
        return s

    def __repr__(self):
        """ representation of the object to be copied """
        return 'Rectangle(%d, %d)'.format(self.__width, self.__height)

    def __del__(self):
        """ delete the instance of the object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width
        Args:
            value: (int): width to check and change with
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter height
        Args:
            value: (int): height to check and change with
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return area rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return perimeter rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Check area of two rectangle
        Args:
            rect_1: (Rectangle): instance of rectangle
            rect_2: (Rectangle): instance of rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            elif rect_1.area() == rect_1.area():
                return rect_1

    @classmethod
    def square(cls, size=0):
        """ class method that return a new instance of rectangle
        Args:
            size: (int): size
        """
        return cls(size, size)
        """
        new = cls()
        new.__width = size
        new.__height = size
        return new"""
