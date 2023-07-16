#!/usr/bin/python3
"""
cosole unit test module
"""

import unittest
from unittest.mock import patch
import io
import sys
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = io.StringIO()
        sys.stdout = self.mock_stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_do_create(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_create_missing_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_do_show_missing_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("show")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_missing_instance_id(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("show BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_invalid_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("show MyModel 123")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_no_instance_found(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("show BaseModel 123")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_destroy_missing_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("destroy")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("destroy BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_invalid_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("destroy MyModel 123")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_no_instance_found(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("destroy BaseModel 123")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel()
        obj2.save()
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("all BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertIn(obj1.id, output)
            self.assertIn(obj2.id, output)

    def test_do_all_invalid_class(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("all MyModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd(f"update BaseModel {obj_id} first_name 'Betty'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
        self.assertEqual(obj.name, "first_name")

    def test_do_update_missing_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_update_missing_instance_id(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update BaseModel")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_update_missing_attr_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update BaseModel {obj.id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_missing_attr_value(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update BaseModel {obj.id} first_name")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_do_update_invalid_class_name(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update MyModel 123 name 'new name'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_no_instance_found(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("update BaseModel 123 name 'new name'")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_emptyline(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_do_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")


if __name__ == '__main__':
    unittest.main()
