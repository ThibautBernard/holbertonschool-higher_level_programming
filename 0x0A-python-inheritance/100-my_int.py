#!/usr/bin/python3
""" subclass of int """


class MyInt(int):
    """My int a subclass of int classes"""
    def __eq__(self, other):
        """eq method that perform __ne__ method"""
        return super().__ne__(self)

    def __ne__(self, other):
        """ne method that perform __eq__ method"""
        return super().__eq__(self)
