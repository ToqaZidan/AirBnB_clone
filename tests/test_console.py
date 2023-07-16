#!/usr/bin/python3
"""
console unittest
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unit tests for the HBNBCommand console class."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the help command."""
        with patch('builtins.input', side_effect=['help', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Documented commands (type help <topic>):", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test the quit command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        """Test the create command with missing class name."""
        with patch('builtins.input', side_effect=['create', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class_name(self, mock_stdout):
        """Test the create command with invalid class name."""
        with patch('builtins.input', side_effect=['create Invalid', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class_name(self, mock_stdout):
        """Test the show command with missing class name."""
        with patch('builtins.input', side_effect=['show', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class_name(self, mock_stdout):
        """Test the show command with invalid class name."""
        with patch('builtins.input', side_effect=['show Invalid', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_instance_id(self, mock_stdout):
        """Test the show command with missing instance ID."""
        with patch('builtins.input', side_effect=['show BaseModel', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_instance(self, mock_stdout):
        """Test the show command with nonexistent instance."""
        with patch('builtins.input', side_effect=['show BaseModel 123', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class_name(self, mock_stdout):
        """Test the destroy command with missing class name."""
        with patch('builtins.input', side_effect=['destroy', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class_name(self, mock_stdout):
        """Test the destroy command with invalid class name."""
        with patch('builtins.input', side_effect=['destroy Invalid', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_instance_id(self, mock_stdout):
        """Test the destroy command with missing instance ID."""
        with patch('builtins.input', side_effect=['destroy BaseModel', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_nonexistent_instance(self, mock_stdout):
        """Test the destroy command with nonexistent instance."""
        with patch('builtins.input', side_effect=['destroy BaseModel 123', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class_name(self, mock_stdout):
        """Test the all command with invalid class name."""
        with patch('builtins.input', side_effect=['all Invalid', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class_name(self, mock_stdout):
        """Test the update command with missing class name."""
        with patch('builtins.input', side_effect=['update', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class_name(self, mock_stdout):
        """Test the update command with invalid class name."""
        with patch('builtins.input', side_effect=['update Invalid', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_instance_id(self, mock_stdout):
        """Test the update command with missing instance ID."""
        with patch('builtins.input', side_effect=['update BaseModel', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_nonexistent_instance(self, mock_stdout):
        """Test the update command with nonexistent instance."""
        with patch('builtins.input', side_effect=['update BaseModel 123', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute_name(self, mock_stdout):
        """Test the update command with missing attribute name."""
        with patch('builtins.input', side_effect=['update BaseModel 123', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """Test the update command with missing value."""
        with patch('builtins.input', side_effect=['update BaseModel 123 attr', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** value missing **")


if __name__ == '__main__':
    unittest.main()
