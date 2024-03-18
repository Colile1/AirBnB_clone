#!/usr/bin/python3
"""
This module creates a class FileStorage
Serializes and deserializes instances
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj in __objects with key <obj class name>.id

        Args:
            obj: Object to be added to dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as file:
                json_objects = json.load(file)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review

                for key, obj_dict in json_objects.items():
                    obj_class = obj_dict["__class__"]
                    if obj_class == "BaseModel":
                        self.__objects[key] = BaseModel(**obj_dict)
                    elif obj_class == "User":
                        self.__objects[key] = User(**obj_dict)
                    elif obj_class == "State":
                        self.__objects[key] = State(**obj_dict)
                    elif obj_class == "City":
                        self.__object[key] = City(**obj_dict)
                    elif obj_class == "Amenity":
                        self.__object[key] = Amenity(**obj_dict)
                    elif obj_class == "Place":
                        self.__object[key] = Place(**obj_dict)
                    elif obj_class == "Review":
                        self.__object[key] = Review(**obj_dict)

        except FileNotFoundError:
            pass
