#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis }
client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache():
    """
    Main class for cache
    """
    def __init__(self):
        """ CONSTRUCTOR"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data as argumen a store in a REDIS db
        Remember that data can be a str, bytes, int or float.

        Returns: A key in string format
        """
        _randomkey = uuid4().__str__()
        self._redis.set(_randomkey, data)
        return _randomkey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_int(self, data: int) -> int:
        try:
            int(data)
            return data
        except Exception:
            return 0

    def get_str(self, data: str) -> str:
        return self._redis.get(data).decode('utf_8')
