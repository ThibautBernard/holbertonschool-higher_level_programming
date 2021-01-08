#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unit test to the function max integer"""
    def test_empty_list(self):
        self.assertEqual(None, max_integer())
    def test_negative_number(self):
        self.assertEqual(-1, max_integer([-10, -2, -3, -1]))
        self.assertEqual(100, max_integer([-10, -2, -3, -1, 10, 100]))
    def test_float(self):
        self.assertEqual(2.9, max_integer([2.5, 2.9]))
        self.assertEqual(5, max_integer([2.5, 2.9, 3, 3.5, 5]))
    def test_one_integer(self):
        self.assertEqual(12, max_integer([12]))
        self.assertEqual(200, max_integer([200]))
        self.assertEqual(0, max_integer([0]))
    def test_zero(self):
        self.assertEqual(0, max_integer([-5, -6, 0]))
    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([-5, "dd", 0])
            max_integer(["dz", "dd", 0])
    def test_only_string(self):
        self.assertEqual("u", max_integer("thibaut"))
        self.assertEqual("z", max_integer("iijzdiojj"))
    def test_only_string_array(self):
        self.assertEqual("thibaut", max_integer(["thibaut"]))
    def test_only_string_array(self):
        with self.assertRaises(TypeError):
            self.assertEqual("z", max_integer(['z', 2]))
    
