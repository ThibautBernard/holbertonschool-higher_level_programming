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
          Area value test cases
        *****************************
    """
    def test_area_with_width_and_height_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(2, 5)
        self.assertEqual(10, t.area())

    def test_area_with_multiple_arg_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(10, t.area())

    def test_area_with_negative_instance(self):
        """
            Test with one instance
        """
        with self.assertRaises(ValueError):
            t = Rectangle(2, -4, 0, 0, 12)

    def test_area_with_x_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(2, 5, 2, 0, 12)
        self.assertEqual(20, t.area())

    def test_area_with_y_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(10, t.area())

    def test_area_with_x_y_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(1, 1, 1, 1, 12)
        self.assertEqual(4, t.area())

    def test_area_with_multiple_instance(self):
        """
            Test with one instance
        """
        t = Rectangle(3, 2)
        u = Rectangle(2, 10)
        x = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(6, t.area())
        self.assertEqual(20, u.area())
        self.assertEqual(56, x.area())

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

    def test_negative_width_setter(self):
        """
            Test return getter with negative
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 2)

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

    def test_Zero_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

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
        with self.assertRaises(ValueError):
            r = Rectangle(-5, -7)

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
        r = Rectangle(3, 5)
        r.height = 9
        self.assertEqual(9, r.height)

    def test_Zero_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

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
        with self.assertRaises(ValueError):
            r = Rectangle(7, 4, -1)

    def test_default_x_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(2, 3)
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
        r = Rectangle(5, 5)
        r.x = 9
        self.assertEqual(9, r.x)

    def test_Zero_x_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(5, 5, 0)
        self.assertEqual(0, r.x)

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
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 5, -5)

    def test_default_y_getter(self):
        """
            Test return getter with negative
        """
        r = Rectangle(9, 9)
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
        r = Rectangle(2, 2)
        r.y = 9
        self.assertEqual(9, r.y)

    def test_assign_string__y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 3)
            r.y = "tt"

    def test_Zero_y_setter(self):
        """
            Test exception with setter other than int
        """
        r = Rectangle(5, 5, 5, 0)
        self.assertEqual(0, r.y)
