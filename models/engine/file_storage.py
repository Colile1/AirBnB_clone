#!/usr/bin/python3
"""Defines the FileStorage class."""
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
    Represent an abstracted storage engine.

    Attributes:
        __file_path (str): name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    
    Methods:
        all(self) -> dict: returns all the objects in the FileStorage.
        new(self, obj) -> None: sets in __objects obj with key <obj_class_name>.id
        save(self) -> None: serializes __objects to the JSON file __file_path
        reload(self) -> None: deserializes the JSON file __file_path to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return a dictionary of all objects in the file storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        A function to add a new object to the FileStorage __objects dictionary.
        
        :param obj: The object to be added to the dictionary.
        :return: None
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Save the objects to a JSON file.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Reloads the objects from the JSON file if it exists, and populates
        the FileStorage.__objects dictionary with the current session with the objects. 
        If the file does not exist, the function returns without doing anything.
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
