#!/usr/bin/python3
"""
Class test of class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Test case for the Rectangle Classes
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    """
        ****************************
          Instance object counter tests cases
        *****************************
    """
    def test_counter_one_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(1, 2)
        self.assertEqual(1, t.id)

    def test_counter_two_instance(self):
        """
            Test with two instance
        """
        u = Rectangle(1, 2)
        t = Rectangle(1, 2)
        self.assertEqual(1, u.id)
        self.assertEqual(2, t.id)

    """
        ****************************
          Width param tests cases
        *****************************
    """

    def test_width_getter(self):
        """
            Test return getter with one int
        """
        r = Rectangle(1, 2)
        self.assertEqual(1, r.width)

    def test_negative_width_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, 2)
        self.assertEqual(-5, r.width)

    def test_list_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle([1], 2)

    def test_string_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle("tt", 2)

    def test_None_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(None, 2)

    def test_assignNumber_width_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(-5, -7)
        r.width = 9
        self.assertEqual(9, r.width)

    """
        ****************************
          Height param tests cases
        *****************************
    """

    def test_height_getter(self):
        """
            Test return getter with one int
        """
        r = Rectangle(1, 2)
        self.assertEqual(2, r.height)

    def test_negative_height_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, -7)
        self.assertEqual(-7, r.height)

    def test_list_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, [2])

    def test_string_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, "td")

    def test_None_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, None)

    def test_assignNumber_height_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(-5, -7)
        r.height = 9
        self.assertEqual(9, r.height)

    """
        ****************************
          X param tests cases
        *****************************
    """

    def test_x_getter(self):
        """
            Test return getter with one int
        """
        r = Rectangle(1, 2, 3)
        self.assertEqual(3, r.x)

    def test_negative_x_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, -7, -4)
        self.assertEqual(-4, r.x)

    def test_default_x_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, -7)
        self.assertEqual(0, r.x)

    def test_list_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, [2])

    def test_string_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 4, "x")

    def test_None_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 6, None)

    def test_assignNumber_x_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(-5, -7)
        r.x = 9
        self.assertEqual(9, r.x)
    """
        ****************************
          Y param tests cases
        *****************************
    """

    def test_y_getter(self):
        """
            Test return getter with one int
        """
        r = Rectangle(1, 2, 3, 6)
        self.assertEqual(6, r.y)

    def test_negative_y_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, -7, -4, -5)
        self.assertEqual(-5, r.y)

    def test_default_y_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(-5, -7)
        self.assertEqual(0, r.y)

    def test_list_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 5, [3])

    def test_string_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 4, 12, "x")

    def test_None_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 6, 8, None)

    def test_assignNumber_y_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(-5, -7)
        r.y = 9
        self.assertEqual(9, r.y)

    def test_assign_string__y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(-5, -7)
            r.y = "tt"
