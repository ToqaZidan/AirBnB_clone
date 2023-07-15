#!/usr/bin/python3
"""
the command-line/console interface module for hbnb system
"""
import cmd
from models.base_model import BaseModel
from models import storage


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
