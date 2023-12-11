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

    @staticmethod
    def save_to_file(cls, list_objs):
        """Saves the list objects into a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dic_list = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(dic_list))
