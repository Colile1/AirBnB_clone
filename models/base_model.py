#!/usr/bin/python3
"""Defines all common attributes/methods
for other classes in the tests package."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class for all models
    """

    def __init__(self, *args, **kwargs):
        """
    	Initialize the object with optional arguments.
    	
    	Parameters:
    	*args: Variable length argument list.
    	**kwargs: Arbitrary keyword arguments.
        
    	Returns:
    	None
    	"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Update updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the object,
        including its created_at and updated_at timestamps.
        """
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
