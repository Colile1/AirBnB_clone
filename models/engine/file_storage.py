#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    A class that serialize and deserialize instances to a JSON file
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method that returns all objects stored in the FileStorage instance.
        """

        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Saves the current state of the objects to a file.

        This function serializes the current state of the objects
        stored in the `__objects` dictionary and writes it to a file
        specified by the `__file_path` attribute. The serialization process
        converts the objects into a dictionary format using the `to_dict()`
        method of each object. The resulting dictionary is then
        written to the file in JSON format using the `json.dump()` function.

        Parameters:
            self (FileStorage): The current instance of the `FileStorage` class

        Returns:
            None
        """

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Method to reload objects from a JSON file into the current session.
        """

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
