#!/usr/bin/python3
"""
Module:console.py
"""

import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Create commande cmd
    """
    prompt = '(hbnb) '

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
    
        if args != BaseModel:
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
        istance_id = args[1]
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                key = "[{}] ({}) {}".format(
                class_name, istance_id)
                if key in data:
                    print(data[key])
                else:
                    print("** no instance found **")
        except FileNotFoundError:
            print("** no file found **")
                
    def do_destroy(self, arg):
        """
        destroy an instance with ID
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
        instance_id = args[1]
        with open(self.__file_path, "r") as file:
            data = json.load(file)
            key = "[{}] ({}) {}".format(
                class_name, instance_id)
            if key not in data:
                print("** no instance found **")
            else:
                del data[key]
                
    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """ 
        args = arg.split()
        if args == BaseModel or args == 0:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                instances = [key and v for key, v in data.items()]
                print(str(instances))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance
        """ 
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != BaseModel:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **") 
            return 
        instance_id = args[1]
        with open(self.__file_path, "r") as file:
            data = json.load(file)
            key = "[{}] ({}) {}".format(
                class_name, instance_id)
            if key not in data:
                print("** no instance found **")
                return
        if len(args) < 3:
            print("** attribute name missing **") 
            return   
        if len(args) < 4:
            print("** value missing **") 
            return
        attribute_name = args[2]
        attribute_value = args[3]
        data[key][attribute_name] = attribute_value
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
