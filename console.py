#!/usr/bin/python3
"""
the command-line/console interface module for hbnb system
"""
import cmd
from models.base_model import BaseModel
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for managing objects in a persistent storage.

    Attributes:
        prompt (str): The prompt string displayed to the user.
    """

    prompt = "(hbnb) "

    def do_create(self, class_name):
        if class_name:
            try:
                obj = globals()[class_name]()
                obj.save
                print(obj.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        arr = line.split()
        try:
            class_name = arr[0]
            try:
                if globals()[class_name]:
                    try:
                        class_id = arr[1]
                        try:
                            key = class_name + "." + class_id
                            print(storage._FileStorage__objects[key])
                        except KeyError:
                            print("** no instance found **")
                    except IndexError:
                        print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")
        except IndexError:
            print("** class name missing **")

    def do_destroy(self, line):
        arr = line.split()
        print(arr)
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
            del objects[key]
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
