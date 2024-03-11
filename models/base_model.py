#!/usr/bin/python3
"""Defines all common attributes/methods for other classes in the tests package."""
import uuid
import models
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
        if kwargs:
            dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], dtime_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], dtime_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # as instructed also in task 5

    def __str__(self):
    	"""
    	Return a string representation of the object.
    	"""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
    	"""
    	Saves the current instance and update the 'updated_at' 
        attribute with the current datetime.
    	"""


        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary that contains all
        keys/values of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__

        return (my_dict)
