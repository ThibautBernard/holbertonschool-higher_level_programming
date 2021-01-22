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
             to_dictionnary()  test cases
        *****************************
    """
    def test_dictionnary_instance(self):
        """
            Test dictionnary
        """
        t = Rectangle(5, 7)
        x = "{'x': 0, 'id': 1, 'width': 5, 'height': 7, 'y': 0}"
        self.assertTrue(type(t.to_dictionary()) is dict)

    """
        ****************************
             .Update  test cases
        *****************************
    """
    def test_update_id_args_instance(self):
        """
            Test update method with
            id
        """
        t = Rectangle(1, 1)
        t.update(25)
        x = "[Rectangle] (25) 0/0 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_width_args_instance(self):
        """
            Test update method with
            width
        """
        t = Rectangle(1, 1)
        t.update(1, 8)
        x = "[Rectangle] (1) 0/0 - 8/1"
        self.assertEqual(x, str(t))

    def test_update_height_args_instance(self):
        """
            Test update method with
            height
        """
        t = Rectangle(1, 1)
        t.update(1, 1, 15)
        x = "[Rectangle] (1) 0/0 - 1/15"
        self.assertEqual(x, str(t))

    def test_update_x_args_instance(self):
        """
            Test update method with
            x
        """
        t = Rectangle(1, 1)
        t.update(1, 1, 1, 15)
        x = "[Rectangle] (1) 15/0 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_y_args_instance(self):
        """
            Test update method with
            y
        """
        t = Rectangle(1, 1)
        t.update(1, 1, 1, 1, 15)
        x = "[Rectangle] (1) 1/15 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_more_than_5_args_instance(self):
        """
            Test update method with
            y
        """
        t = Rectangle(1, 1)
        t.update(1, 1, 1, 1, 1, 6, 84)
        x = "[Rectangle] (1) 1/1 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_string_args_instance(self):
        """
            Test update method with
            string
        """
        with self.assertRaises(TypeError):
            t = Rectangle(1, 1)
            t.update(5, "dzdz", 1, 1, 1)

    def test_update_negative_args_instance(self):
        """
            Test update method with
            negative
        """
        with self.assertRaises(ValueError):
            t = Rectangle(1, 1)
            t.update(5, 1, -4, 1, 1)

    def test_update_list_args_instance(self):
        """
            Test update method with
            list
        """
        with self.assertRaises(TypeError):
            t = Rectangle(1, 1)
            t.update(5, ['1'])

    def test_update_width_error_msg_args_instance(self):
        """
            Test update method with
            list
        """
        x = "width must be an integer"
        with self.assertRaises(TypeError) as cm:
            t = Rectangle(1, 1)
            t.update(5, ['1'])
        self.assertEqual(x, str(cm.exception))

    def test_update_y_error_msg_args_instance(self):
        """
            Test update method with
            string
        """
        y = "y must be an integer"
        with self.assertRaises(TypeError) as cm:
            t = Rectangle(1, 1)
            t.update(5, 6, 7, 2, "str")
        self.assertEqual(y, str(cm.exception))

    def test_update_y_error_msg_args_instance(self):
        """
            Test update method with
            value negative
        """
        y = "y must be >= 0"
        with self.assertRaises(ValueError) as cm:
            t = Rectangle(1, 1)
            t.update(5, 6, 7, 2, -5)
        self.assertEqual(y, str(cm.exception))

    def test_update_width_error_msg_args_instance(self):
        """
            Test update method with
            value negative
        """
        w = "width must be > 0"
        with self.assertRaises(ValueError) as cm:
            t = Rectangle(1, 1)
            t.update(5, 0)
        self.assertEqual(w, str(cm.exception))

    def test_update_width_kwargs_instance(self):
        """
            Test update method with
            kwargs width
        """
        t = Rectangle(1, 1)
        t.update(width=5)
        x = "[Rectangle] (1) 0/0 - 5/1"
        self.assertEqual(x, str(t))

    def test_update_y_kwargs_instance(self):
        """
            Test update method with
            kwargs y
        """
        t = Rectangle(1, 1)
        t.update(y=5)
        x = "[Rectangle] (1) 0/5 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_multiple_kwargs_instance(self):
        """
            Test update method with
            kwargs multiple
        """
        t = Rectangle(1, 1)
        t.update(y=5, width=12, x=9)
        x = "[Rectangle] (1) 9/5 - 12/1"
        self.assertEqual(x, str(t))

    def test_update_args_and_kwargs_instance(self):
        """
            Test update method with
            kwargs width
        """
        t = Rectangle(1, 1)
        t.update(2, y=5, width=12, x=9)
        x = "[Rectangle] (2) 0/0 - 1/1"
        self.assertEqual(x, str(t))

    def test_update_kwargs_error_msg_string_instance(self):
        """
            Test update kwargs error msg with string
        """
        w = "width must be an integer"
        with self.assertRaises(TypeError) as cm:
            t = Rectangle(1, 1)
            t.update(width="54")
        self.assertEqual(w, str(cm.exception))

    def test_update_kwargs_error_msg_Zero_instance(self):
        """
            Test update kwargs error msg with 0
        """
        w = "width must be > 0"
        with self.assertRaises(ValueError) as cm:
            t = Rectangle(1, 1)
            t.update(width=0)
        self.assertEqual(w, str(cm.exception))

    def test_update_kwargs_more_arguments_instance(self):
        """
            Test update kwargs more arguments than exist
        """
        t = Rectangle(1, 1)
        t.update(width=3, height=3, y=2, x=2, id=90, z=5)
        x = "[Rectangle] (90) 2/2 - 3/3"
        self.assertEqual(x, str(t))

    """
        ****************************
        Str representation test cases
        *****************************
    """

    def test_str_width_only_width_instance(self):
        """
            Test __str__ return with width
        """
        t = Rectangle(2, 1)
        x = "[Rectangle] (1) 0/0 - 2/1"
        self.assertEqual(x, str(t))

    def test_str_width_id_instance(self):
        """
            Test __str__ return with width
            id = 3
        """
        t = Rectangle(2, 1, 0, 0, 3)
        x = "[Rectangle] (3) 0/0 - 2/1"
        self.assertEqual(x, str(t))

    """
        ****************************
        Display rectangle test cases
        *****************************
    """
    def test_display_with_Zero_height_instance(self):
        """
            Test zero in height param
        """
        with self.assertRaises(ValueError):
            t = Rectangle(2, 0)

    def test_display_with_Zero_width_instance(self):
        """
            Test zero in width param
        """
        with self.assertRaises(ValueError):
            t = Rectangle(0, 1)

    """
        ****************************
          Area value test cases
        *****************************
    """
    def test_area_with_width_and_height_instance(self):
        """
            Test area with only width/height
        """
        t = Rectangle(2, 5)
        self.assertEqual(10, t.area())

    def test_area_with_multiple_arg_instance(self):
        """
            Test area with all param
        """
        t = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(10, t.area())

    def test_area_with_negative_instance(self):
        """
            Test area with negative heigth
        """
        with self.assertRaises(ValueError):
            t = Rectangle(2, -4, 0, 0, 12)

    def test_area_with_x_instance(self):
        """
            Test area with x param
        """
        t = Rectangle(2, 5, 2, 0, 12)
        self.assertEqual(10, t.area())

    def test_area_with_y_instance(self):
        """
            Test area with y param
        """
        t = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(10, t.area())

    def test_area_with_x_y_instance(self):
        """
            Test are with x and y param
        """
        t = Rectangle(1, 1, 1, 1, 12)
        self.assertEqual(1, t.area())

    def test_area_with_multiple_instance(self):
        """
            Test area with multiple instance
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
