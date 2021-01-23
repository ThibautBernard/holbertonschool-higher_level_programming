#!/usr/bin/python3
"""
Class test of class Square
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Test case for the Square Classes
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
        t = Square(1, 2)
        self.assertEqual(1, t.id)

    def test_counter_two_instance(self):
        """
            Test with two instance
        """
        u = Square(1, 2)
        t = Square(1, 2)
        self.assertEqual(1, u.id)
        self.assertEqual(2, t.id)

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
        t = Square(1, 1)
        t.update(25)
        x = "[Square] (25) 1/0 - 1"
        self.assertEqual(x, str(t))

    def test_update_size_args_instance(self):
        """
            Test update method with
            size
        """
        t = Square(1, 1)
        t.update(1, 8)
        x = "[Square] (1) 1/0 - 8"
        self.assertEqual(x, str(t))

    def test_update_x_args_instance(self):
        """
            Test update method with x
        """
        t = Square(1, 1)
        t.update(1, 1, 7)
        x = "[Square] (1) 7/0 - 1"
        self.assertEqual(x, str(t))

    def test_update_string_exception_instance(self):
        """
            Test exception update size by a string
        """
        with self.assertRaises(TypeError):
            t = Square(2, 1)
            t.update(5, "5454")

    def test_update_negative_exception_instance(self):
        """
            Test exception update size by a negative
        """
        with self.assertRaises(ValueError):
            t = Square(2, 1)
            t.update(5, -5)

    def test_update_Zero_exception_instance(self):
        """
            Test exception update size by a Zero
        """
        with self.assertRaises(ValueError):
            t = Square(2, 1)
            t.update(5, 0)

    def test_update_id_kwargs_instance(self):
        """
            Test update kwargs method with id
        """
        t = Square(1, 1)
        t.update(id=80)
        x = "[Square] (80) 1/0 - 1"
        self.assertEqual(x, str(t))

    def test_update_multiple_kwargs_instance(self):
        """
            Test update kwargs method with multiple
        """
        t = Square(1, 1)
        t.update(id=80, size=5, y=3)
        x = "[Square] (80) 1/3 - 5"
        self.assertEqual(x, str(t))

    def test_update_negative_kwargs_instance(self):
        """
            Test update kwargs method with negative
        """
        with self.assertRaises(ValueError):
            t = Square(1, 1)
            t.update(id=80, size=-1, y=3)
            x = "[Square] (80) 1/3 - 5"

    def test_update_args_and_kwargs_instance(self):
        """
            Test update kwargs method with args and kwargs
        """
        t = Square(1, 1)
        t.update(5, id=80)
        x = "[Square] (5) 1/0 - 1"
        self.assertEqual(x, str(t))

    def test_update_None_kwargs_instance(self):
        """
            Test update kwargs method with None
        """
        with self.assertRaises(TypeError):
            t = Square(1, 1)
            t.update(size=None, y=3)
            x = "[Square] (80) 1/3 - 5"

    """
        ****************************
             to_dictionnary()  test cases
        *****************************
    """
    def test_dictionnary_instance(self):
        """
            Test dictionnary
        """
        t = Square(5, 7)
        self.assertTrue(type(t.to_dictionary()) is dict)

    """
        ****************************
        Size attribut assign & setter test cases
        *****************************
    """

    def test_size_setter_instance(self):
        """
            Test size setter and representation str()
        """
        t = Square(2, 1)
        t.size = 5
        x = "[Square] (1) 1/0 - 5"
        self.assertEqual(x, str(t))

    def test_size_setter_and_getter_init_instance(self):
        """
            Test size setter and getter at __init__
        """
        t = Square(10, 1)
        self.assertEqual(10, t.size)

    def test_size_setter_negative_error_instance(self):
        """
            Test size setter with negative and exception raised
        """
        with self.assertRaises(ValueError):
            t = Square(2, 1)
            t.size = -5

    def test_size_setter_string_error_instance(self):
        """
            Test size setter with string and exception raised
        """
        with self.assertRaises(TypeError):
            t = Square(2, 1)
            t.size = "5"

    def test_size_setter_string_error_msg_instance(self):
        """
            Test size msg exception setter assign with string
        """
        x = "width must be an integer"
        with self.assertRaises(TypeError) as cm:
            t = Square(1, 1)
            t.size = "54"
        self.assertEqual(x, str(cm.exception))

    def test_size_setter_Zero_error_msg_instance(self):
        """
            Test size msg exception setter assign with string
        """
        x = "width must be > 0"
        with self.assertRaises(ValueError) as cm:
            t = Square(1, 1)
            t.size = 0
        self.assertEqual(x, str(cm.exception))
    """
        ****************************
        Str representation test cases
        *****************************
    """

    def test_str_width_only_width_instance(self):
        """
            Test __str__ return with width
        """
        t = Square(2, 1)
        x = "[Square] (1) 1/0 - 2"
        self.assertEqual(x, str(t))

    def test_str_width_id_instance(self):
        """
            Test __str__ return with width
            id = 3
        """
        t = Square(2, 1, 0, 3)
        x = "[Square] (3) 1/0 - 2"
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
            t = Square(0)

    def test_display_with_Zero_width_instance(self):
        """
            Test zero in width param
        """
        with self.assertRaises(ValueError):
            t = Square(0)

    """
        ****************************
          Area value test cases
        *****************************
    """
    def test_area_with_width_and_height_instance(self):
        """
            Test area with only width/height
        """
        t = Square(2)
        self.assertEqual(4, t.area())

    def test_area_with_multiple_arg_instance(self):
        """
            Test area with all param
        """
        t = Square(2, 5, 0, 12)
        self.assertEqual(4, t.area())

    def test_area_with_negative_instance(self):
        """
            Test area with negative heigth
        """
        with self.assertRaises(ValueError):
            t = Square(-5)

    def test_area_with_x_y_instance(self):
        """
            Test are with x and y param
        """
        t = Square(1, 1, 1, 12)
        self.assertEqual(1, t.area())

    def test_area_with_multiple_instance(self):
        """
            Test area with multiple instance
        """
        t = Square(3, 2)
        u = Square(2, 10)
        x = Square(8, 7)
        self.assertEqual(9, t.area())
        self.assertEqual(4, u.area())
        self.assertEqual(64, x.area())

    """
        ****************************
          Width param tests cases
        *****************************
    """

    def test_width_getter(self):
        """
            Test return getter with one int
        """
        r = Square(1, 2)
        self.assertEqual(1, r.width)

    def test_negative_width_setter(self):
        """
            Test return getter with negative
        """
        with self.assertRaises(ValueError):
            r = Square(-5, 2)

    def test_list_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square([1], 2)

    def test_string_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square("tt", 2)

    def test_None_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(None, 2)

    def test_Zero_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(ValueError):
            r = Square(0, 2)

    """
        ****************************
          Height param tests cases
        *****************************
    """

    def test_height_getter(self):
        """
            Test return getter with one int
        """
        r = Square(2)
        self.assertEqual(2, r.height)

    def test_negative_height_getter(self):
        """
            Test return getter with negative
        """
        with self.assertRaises(ValueError):
            r = Square(-7)

    def test_list_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square([2])

    def test_string_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square("td")

    def test_None_height_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(None)

    def test_assignNumber_height_setter(self):
        """
            Test exception with setter other than int
        """
        r = Square(3, 9)
        r.height = 5
        self.assertEqual(5, r.height)

    def test_Zero_width_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(ValueError):
            r = Square(0)

    """
        ****************************
          X param tests cases
        *****************************
    """

    def test_x_getter(self):
        """
            Test return getter with one int
        """
        r = Square(1, 2)
        self.assertEqual(2, r.x)

    def test_negative_x_getter(self):
        """
            Test return getter with negative
        """
        with self.assertRaises(ValueError):
            r = Square(7, -1)

    def test_default_x_getter(self):
        """
            Test return getter with default value
        """
        r = Square(2)
        self.assertEqual(0, r.x)

    def test_list_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(2, [2])

    def test_string_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(2, "x")

    def test_None_x_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(3, None)

    def test_assignNumber_x_setter(self):
        """
            Test exception with setter with assignment
        """
        r = Square(5, 3)
        r.x = 9
        self.assertEqual(9, r.x)

    def test_Zero_x_setter(self):
        """
            Test exception with setter other than int
        """
        r = Square(5, 0)
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
        r = Square(1, 2, 3)
        self.assertEqual(3, r.y)

    def test_negative_y_getter(self):
        """
            Test return getter with negative
        """
        with self.assertRaises(ValueError):
            r = Square(3, 4, -5)

    def test_default_y_getter(self):
        """
            Test return getter with negative
        """
        r = Square(9, 9)
        self.assertEqual(0, r.y)

    def test_list_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(2, 3, [3])

    def test_string_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(2, 4, "x")

    def test_None_y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(3, 6, None)

    def test_assignNumber_y_setter(self):
        """
            Test exception with setter other than int
        """
        r = Square(2, 2, 7)
        r.y = 9
        self.assertEqual(9, r.y)

    def test_assign_string__y_setter(self):
        """
            Test exception with setter other than int
        """
        with self.assertRaises(TypeError):
            r = Square(3, 3, 8)
            r.y = "tt"

    def test_Zero_y_setter(self):
        """
            Test exception with setter other than int
        """
        r = Square(5, 5, 0)
        self.assertEqual(0, r.y)
