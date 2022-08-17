#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis }
client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

"""

from redis import Redis
from typing import Union


class Cache():
    """
    Main clas
    """
    _redis = Redis()
    _redis.flushdb()

    def store(self, data: Union['str', 'bytes', 'int', 'float']) -> str:
        """
        Takes a data as argumen
        Remember that data can be a str, bytes, int or float.

        Returns: A string
        """
        import uuid

        __TYPES = ['str', 'bytes', 'int', 'float']

        if data.__class__.__name__ in __TYPES:
            _randomkey = uuid.uuid4().__str__()
            self._redis.set(_randomkey, data)
            return _randomkey
        else:
            return None
