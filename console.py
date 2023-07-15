#!/usr/bin/python3
"""
the command-line/console interface module for hbnb system
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for managing objects in a persistent storage.

    Attributes:
        prompt (str): The prompt string displayed to the user.
    """

    prompt = "(hbnb) "

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
