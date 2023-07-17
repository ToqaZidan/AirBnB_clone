#!/usr/bin/python3
"""
This module contains the command-line/console interface for the HBNB system.
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sys
import re
import json


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for managing objects in
    a persistent storage.

    Attributes:
        prompt (str): The prompt string displayed to the user.
    """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Parses command line input and converts it to a standard format.

        Args:
            line (str): The command line input.

        Returns:
            str: The standardized command line input, or the original input
            if it does not match the expected format.
        """
        if not ('.' in line and '(' in line and ')' in line):
            return line

        pattern = (r'^(\w*)\.(\w+)\("?([\w-]*)"?,?'
                   r' ?"?(\{?[\w ,\"\':-]*\}?)"?\}?,? ?"?([\w-]*)"?\)$')

        match = re.match(pattern, line)
        if match:
            class_name = match.group(1)
            command = match.group(2)
            id = match.group(3)
            attr_name = match.group(4)
            attr_value = match.group(5)

            # find if string is a dictionary
            try:
                if isinstance(eval(attr_name), dict):
                    new_str = ''
                    for i in attr_name:
                        if i != ' ':
                            new_str += i
                    attr_name = new_str
            except Exception:
                pass
            return f"{command} {class_name} {id} {attr_name} {attr_value}"
        else:
            return line

    def postloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_create(self, class_name):
        """
        Creates a new instance of a specified class.

        Args:
            class_name (str): The name of the class to
            create an instance of.

        Usage:
            create <class_name>
        """
        if class_name:
            try:
                obj = globals()[class_name]()
                obj.save()
                print(obj.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Displays the details of a specified instance.

        Args:
            line (str): The command line input.

        Usage:
            show <class_name> <instance_id>
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes a specified instance.

        Args:
            line (str): The command line input.

        Usage:
            destroy <class_name> <instance_id>
        """
        arr = line.split()

        if len(arr) < 1:
            print("** class name missing **")
            return

        class_name = arr[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arr) < 2:
            print("** instance id missing **")
            return

        obj_id = arr[1]
        key = f"{class_name}.{obj_id}"

        objects = storage.all()
        if key in objects:
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, line):
        """
        Displays all instances of a specified class,
        or all instances if no class is specified.

        Args:
            line (str): The command line input.

        Usage:
            all [<class_name>]
        """
        arr = line.split()
        objects = storage.all()
        all_list = []

        if len(arr) < 1:
            for k in objects:
                all_list.append(str(objects[k]))
            print(all_list)
            return

        class_name = arr[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arr) < 2:
            for k in objects:
                if class_name in k:
                    all_list.append(str(objects[k]))
            print(all_list)
            return

    def do_update(self, line):
        """
        Updates the attributes of a specified instance.

        Args:
            line (str): The command line input.

    Usage:
        update <cls_name> <id> <attr_name> <attr_value>
        """
        arr = line.split()

        if len(arr) < 1:
            print("** class name missing **")
            return

        class_name = arr[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arr) < 2:
            print("** instance id missing **")
            return

        obj_id = arr[1]
        key = f"{class_name}.{obj_id}"

        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(arr) < 3:
            print("** attribute name missing **")
            return

        obj_attr = arr[2]
        new_obj = storage.all()[key]

        try:
            if isinstance(eval(obj_attr), dict):
                for k, v in eval(obj_attr).items():
                    new_obj.__dict__.update({k: v})
                new_obj.save()
                return
        except Exception:
            pass

        if len(arr) < 4:
            print("** value missing **")
            return

        obj_val = ' '.join(arr[3:])
        if obj_val[0] == obj_val[-1] == '"':
            obj_val = obj_val[1:-1]
        obj_val = obj_val.replace('\\"', '"')

        new_obj.__dict__.update({obj_attr: obj_val})
        new_obj.save()

    def do_count(self, line):
        """
        Counts the number of instances of a specified class.

        Args:
            line (str): The command line input.

        Usage:
            count <class_name>

        Returns:
            None
        """
        arr = line.split()
        objects = storage.all()
        count = 0

        if len(arr) < 1:
            print("** class name missing **")
            return

        class_name = arr[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        for k in objects:
            if class_name in k:
                count += 1
        print(count)
        return

    def do_quit(self, line):
        """
        Exits the program.

        Usage:
            quit
        """
        return True

    def do_EOF(self, line):
        """
        Exits the programif the user types in EOF (Ctrl+D).

        Usage:
            Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        return

    def help_create(self):
        """
        Displays help information for the create command.
        """
        print("Creates a new instance of a specified class.")
        print("Usage: create <class_name>")

    def help_show(self):
        """
        Displays help information for the show command.
        """
        print("Displays the details of a specified instance.")
        print("Usage: show <class_name> <instance_id>")

    def help_destroy(self):
        """
        Displays help information for the destroy command.
        """
        print("Deletes a specified instance.")
        print("Usage: destroy <class_name> <instance_id>")

    def help_all(self):
        """
        Displays help information for the all command.
        """
        print("Displays all instances of a specified class,\
                or all instances if no class is specified.")
        print("Usage: all [<class_name>]")

    def help_update(self):
        """
        Displays help information for the update command.
        """
        print("Updates the attributes of a specified instance.")
        print("Usage: update <cls name> <id> <attr name> <attr value>")

    def help_count(self):
        """
        Displays help information for the update command.
        """
        print("Counts the number of instances of a specified class.")
        print("Usage: count <class_name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
