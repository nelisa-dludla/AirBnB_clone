#!/usr/bin/python3
"""This module contains the class HBNBCommand"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBNBCommand class

    Attributes:
        prompt (str): A customize prompt for the command interpreter
        class_name (list): A list of known obj classes

    Methods:
        do_quit(self, args): Exits the program
        do_EOF(self, args): Handles the end-of-file command
        emptyline(self): Does nothing
        do_create(self, *arguments): Creates a new instance of BaseModel
        do_show(self, *arguments): Prints a str representation of the instance
        do_destroy(self, *arguments): Destroys an instance
        do_all(self, args): Prints all string representation of instances
        do_update(self, *arguments): Updates an instance
        do_count(self, args): Retrieves the number of instances of a class
    """
    prompt = "(hbnb) "
    class_names = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

    objs = storage.all()

    def do_quit(self, arg):
        """Exits the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """Handles the end-of-file command"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, *arguments):
        """Creates a new instance of BaseModel"""

        if arguments[0] == "":
            print("** class name missing **")
        else:
            if arguments[0] in HBNBCommand.class_names:
                new_instance = switch_objects(arguments[0])
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, *arguments):
        """Prints a string representation of the instance"""

        args = arguments[0].split(" ")
        objs = storage.all()

        if args[0] == '':
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in objs:
                print("** no instance found **")
            else:
                print(objs[f"{args[0]}.{args[1]}"])

    def do_destroy(self, *arguments):
        """Destroys an instance"""

        args = arguments[0].split(" ")

        if args[0] == '':
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in HBNBCommand.objs:
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                del HBNBCommand.objs[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of instances"""

        all_instances = []
        if args != '':
            if args not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            else:
                for key in HBNBCommand.objs.keys():
                    key_list = key.split(".")
                    if key_list[0] == args:
                        item = HBNBCommand.objs[key]
                        all_instances.append(str(item))

                print(all_instances)
        else:
            for key in HBNBCommand.objs.keys():
                item = HBNBCommand.objs[key]
                all_instances.append(str(item))

            print(all_instances)

    def do_update(self, *arguments):
        """Updates an instance"""

        arg = arguments[0].split(" ")

        if arg[0] == '':
            print("** class name missing **")
        else:
            if arg[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            elif f"{arg[0]}.{arg[1]}" not in HBNBCommand.objs:
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                key = f"{arg[0]}.{arg[1]}"
                setattr(HBNBCommand.objs[key], arg[2], arg[3].strip('"'))

    def default(self, args):
        """
        Alters default to handle specific methods

        Methods:
            all(): Retrieves all class instances
            count(): Retrieves the number of instances of a class
        """

        methods = [
                "all()",
                "count()",
            ]

        arg_list = args.split(".")

        if len(arg_list) > 1:
            class_name, method = arg_list

            if method in methods and class_name in HBNBCommand.class_names:
                self.onecmd(f"{method.strip('()')} {class_name}")
        else:
            pass

    def do_count(self, args):
        """Retrieves the number of instances of a class"""

        all_instances = []
        if args != '':
            if args not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            else:
                for key in HBNBCommand.objs.keys():
                    key_list = key.split(".")
                    if key_list[0] == args:
                        item = HBNBCommand.objs[key]
                        all_instances.append(str(item))

                print(len(all_instances))


def switch_objects(obj_type):
    """Returns the object for the specified type"""

    if obj_type == "BaseModel":
        return BaseModel()
    elif obj_type == "User":
        return User()
    elif obj_type == "State":
        return State()
    elif obj_type == "City":
        return City()
    elif obj_type == "Amenity":
        return Amenity()
    elif obj_type == "Place":
        return Place()
    elif obj_type == "Review":
        return Review()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
