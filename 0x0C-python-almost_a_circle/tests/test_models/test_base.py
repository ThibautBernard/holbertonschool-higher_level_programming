#!/usr/bin/python3
"""
Class test of class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os.path
from os import path


class TestBase(unittest.TestCase):
    """
        Test case for the Base Classes
    """
    def setUp(self):
        """ Reset class attribute """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Delete files create """
        if path.exists("Square.json"):
            os.remove("Square.json")
        if path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

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
        self.assertEqual(1, b1.id)

    def test_C_mul_instance_no_arg(self):
        """
            Test counter with multiple instance
        """
        c1 = Base()
        c2 = Base()
        c3 = Base()
        self.assertEqual(3, c3.id)

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

    def test_arg_mul_nb_object_instance(self):
        """
            Test multiple instance with arg
        """
        x = Base(10)
        z = Base()
        p = Base(3)
        self.assertEqual(10, x.id)
        self.assertEqual(1, z.id)
        self.assertEqual(3, p.id)

    def test_arg_multiple_instance(self):
        """
            Test multiple instance with arg
        """
        a = Base()
        b = Base()
        c = Base()
        d = Base(6)
        e = Base()
        f = Base()
        g = Base()
        h = Base()
        i = Base()
        self.assertEqual(8, i.id)


        """
            ****************
             TO_JSON_STRING
            ****************
        """

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

        """
            ****************
              SAVE_TO_FILE
            ****************
        """
    def test_save_to_file_empty_arg_instance(self):
        """
            Test savetofile method if empty arg
        """
        r = Rectangle(1, 1)
        Rectangle.save_to_file(None)
        self.assertTrue(path.exists("Base.json"))

    def test_save_to_file_rectangle_arg_instance(self):
        """
            Test savetofile method if empty arg
        """
        r = Rectangle(1, 1)
        Rectangle.save_to_file([r])
        self.assertTrue(path.exists("Rectangle.json"))

        """
            ****************
            FROM_JSON_STRING
            ****************
        """
    def test_from_json_string_str_return_instance(self):
        """
            Test from_json_string()
        """
        l = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(l)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)

    def test_from_json_string_None_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(None)
        lent = len(list_output)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(0, lent)

    def test_from_json_string_Int_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(5)
        self.assertTrue(list_output is None)

    def test_from_json_string_Float_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(5.5)
        self.assertTrue(list_output is None)

    def test_from_json_string_Bool_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(True)
        self.assertTrue(list_output is None)

    def test_from_json_string_list_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(['dd'])
        self.assertTrue(list_output is None)

    def test_from_json_string_Tuple_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string((1, 2))
        self.assertTrue(list_output is None)

    def test_from_json_string_Str_empty_return_instance(self):
        """
            Test from_json_string()
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string("")
        lent = len(list_output)
        self.assertEqual(0, lent)

        """
            ****************
               CREATE()
            ****************
        """
    def test_create_instance_check_type_return_instance(self):
        """
            Test create()
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(type(r2) is Rectangle)

    def test_create_instance_check_value_return_instance(self):
        """
            Test create()
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        s = "[Rectangle] (1) 1/0 - 3/5"
        self.assertEqual(s, str(r2))

    def test_create_instance_negative_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_negative_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_float_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2.5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_tuple_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle((0, 2), 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_string_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("dzdz", 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_array_exception_raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle([2], 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

    def test_create_instance_None_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(None)

    def test_create_instance_String_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create("ddz")

    def test_create_instance_Int_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(2)

    def test_create_instance_Float_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(2.4)

    def test_create_instance_List_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create([2, 2])

    def test_create_instance_Tuple_Exception_Raised_instance(self):
        """
            Test create()
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create((2, 5))

        """
            ****************
               load_from_file()
            ****************
        """
    def test_load_from_file_Rectangle_check_return_instance(self):
        """
            Test load_from_file()
        """
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        new = Rectangle.load_from_file()
        self.assertTrue(type(new[0]) is Rectangle)

    def test_load_from_file_Rectangle_check_value_return_instance(self):
        """
            Test load_from_file()
        """
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        new = Rectangle.load_from_file()
        s = "[Rectangle] (1) 2/8 - 10/7"
        self.assertEqual(s, str(new[0]))

    def test_load_from_file_Square_check_return_instance(self):
        """
            Test load_from_file()
        """
        s1 = Square(5)
        Square.save_to_file([s1])
        new = Square.load_from_file()
        self.assertTrue(type(new[0]) is Square)

    def test_load_from_file_Square_check_value_return_instance(self):
        """
            Test load_from_file()
        """
        s1 = Square(5)
        Square.save_to_file([s1])
        new = Square.load_from_file()
        s = "[Square] (5) 0/0 - 5"
        self.assertEqual(s, str(new[0]))

    def test_load_from_file_Square_check_value_return_instance(self):
        """
            Test load_from_file()
        """
        s1 = Square(5)
        Square.save_to_file([s1])
        new = Square.load_from_file()
        s1.update(20)
        Square.save_to_file([s1])
        new = Square.load_from_file()
        s = "[Square] (20) 0/0 - 5"
        self.assertEqual(s, str(new[1]))

    def test_load_from_file_Square_File_Not_exist_return_instance(self):
        """
            Test load_from_file()
        """
        s1 = Square(5)
        new = Square.load_from_file()
        l = len(new)
        self.assertTrue(type(new) is list)
        self.assertEqual(0, l)
