#!/usr/bin/python3
"""
__init__ constructor method to create a new instance of models directory
and initialized object's attributes.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
