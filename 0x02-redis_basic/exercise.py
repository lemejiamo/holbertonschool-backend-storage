#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis }
client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

"""

import redis
from typing import Union
import uuid


class Cache():
    """
    Main class for cache
    """
    def __init__(self):
        """ CONSTRUCTOR"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union['str', 'bytes', 'int', 'float']) -> str:
        """
        Takes a data as argumen a store in a REDIS db
        Remember that data can be a str, bytes, int or float.

        Returns: A key in string format
        """
        _randomkey = uuid.uuid4().__str__()
        self._redis.set(_randomkey, data)
        return _randomkey
