#!/usr/bin/python3
"""
Module:console.py
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Create commande cmd
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        quit commande to EXIT the program
        """
        return True

    def do_EOF(self, arg):
        """
        Ctrl+d commande to Exit the program
        """
        return True

    def empty_line(self):
        """
        an empty line + ENTER shoudn't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
