#!/usr/bin/python3
"""
Class test of class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
        Test case for the Base Classes
    """
    def test_A_other_none(self):
        """
            Test with None passed
        """
        d1 = Base(None)
        self.assertEqual(1, d1.id)

    def test_B_no_arg_one_object(self):
        """
            Test counter instance
        """
        b1 = Base()
        self.assertEqual(2, b1.id)

    def test_C_mul_instance_no_arg(self):
        """
            Test counter with multiple instance
        """
        c1 = Base()
        c2 = Base()
        c3 = Base()
        self.assertEqual(5, c3.id)

    def test_arg_zero(self):
        """
            Test arg zero
        """
        n = Base(0)
        self.assertEqual(0, n.id)

    def test_arg_negative(self):
        """
            Test arg negative
        """
        x = Base(-4)
        self.assertEqual(-4, x.id)

    def test_arg_mul_instance(self):
        """
            Test multiple instance with arg
        """
        x = Base(10)
        z = Base(5)
        p = Base(3)
        self.assertEqual(10, x.id)
        self.assertEqual(5, z.id)
        self.assertEqual(3, p.id)

    def test_to_json_string_string_return_instance(self):
        """
            Test json to string return
        """
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json = Base.to_json_string(d)
        self.assertTrue(type(json) is str)

    def test_to_json_string_None_return_instance(self):
        """
            Test json to string with None return
        """
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json = Base.to_json_string(None)
        self.assertEqual("[]", json)

    def test_to_json_string_Empty_return_instance(self):
        """
            Test json to string with empty dict return
        """
        json = Base.to_json_string({})
        self.assertEqual("[]", json)

    def test_to_json_string_OtherType_return_instance(self):
        """
            Test json to string with string
        """
        json = Base.to_json_string("dd")
        self.assertEqual(None, json)
