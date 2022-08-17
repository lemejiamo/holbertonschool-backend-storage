#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis }
client as a private variable named _redis (using redis.Redis()) and 
flush the instance using flushdb.

"""

from redis import Redis


class Cache():
    """
    Main clas
    """
    _redis = Redis()
    _redis.flushdb()

    def store(self, data):
        import uuid
        """
        Takes a data as argumen
        Remember that data can be a str, bytes, int or float.

        Returns: A string
        """

        _randomkey = uuid.uuid4().__str__()

        self._redis.set(_randomkey, data)
        return _randomkey
