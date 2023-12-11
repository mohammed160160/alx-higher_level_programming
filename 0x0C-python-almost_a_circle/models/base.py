#!/usr/bin/python3
""""The base of the class system"""
import json


class Base():
    """The base class for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The id system for the program"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"Prints the JSON representation of the dirtionaries list"""
        if list_dictionaries is None:
            return (json.dumps([]))
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the list objects into a JSON file"""
        filename = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for items in list_objs:
                content.append(cls.to_dictionary(items))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """Returns the class representation from a json_string"""
        if (json_string is None) or (len(json_string) == 0):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set
        using a dictionary"""
        if cls.__name__ == 'Rectangle':
            copy = cls(1, 1)
        elif cls.__name__ == 'Square':
            copy = cls(1)
        copy.update(**dictionary)
        return (copy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        filecontent = []
        try:
            with open(filename, 'r') as f:
                content = cls.from_json_string(f.read())
            for items in content:
                filecontent.append(cls.create(**items))
        except FileNotFoundError:
            pass
        return (content)
