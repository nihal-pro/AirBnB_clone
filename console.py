#!/usr/bin/python3
"""
Module:console.py
"""

import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Create commande cmd
    """
    prompt = '(hbnb) '
    __file_path = "file.json"

    def do_quit(self, arg):
        """
        quit commande to EXIT the program
        """
        return True

    def do_EOF(self, line):
        """
        Ctrl+d commande to Exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        an empty line + ENTER shoudn't execute anything
        """
        pass

    def do_help(self, arg):
        """
        help function
        """
        return super().do_help(arg)

    def do_create(self, arg):
        """
        create new instance
        """
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if 'BaseModel' not in args:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show an instance with ID
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        instances = objects.get(key, None)
        if instances is None:
            print("** no instance found **")
            return
        print(instances)

    def do_destroy(self, arg):
        """
        destroy an instance with ID
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        objects = storage.all()

        if len(args) < 1:
            print(["{}".format(v) for _, v in objects.items()])
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(v) for _, v in objects.items()])

    def do_update(self, arg):
        """
        Updates an instance
        """
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instances = objects.get(key, None)
        if instances is None:
            print("** no instance found **")
            return

        setattr(instances, args[2], args[3].lstrip('"').rstrip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
