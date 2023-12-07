#!/usr/bin/python3
"""Module initializes a FileStorage instance"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
