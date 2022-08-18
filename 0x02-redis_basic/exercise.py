#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis }
client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count how many times the function was called
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
        store the history of inputs and outputs for a particular function.
    """

    inputs = '{}:inputs'.format(method.__qualname__)
    outputs = '{}:outputs'.format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper function"""

        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(outputs, output)
        return output
    return wrapper


def replay(methodName: Callable) -> None:
    """
    Display the history of calls of a function
    """

    _redis = redis.Redis()
    try:
        calls = _redis.get(methodName.__qualname__).decode('utf-8')
    except Exception:
        calls = 0

    print(f'{methodName.__qualname__} was called {calls} times:')

    inputs = _redis.lrange(methodName.__qualname__ + ':inputs', 0, -1)
    outputs = _redis.lrange(methodName.__qualname__ + ':outputs', 0, -1)

    for input, output in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(methodName.__qualname__,
                                     input.decode('utf-8'),
                                     output.decode('utf-8')))


class Cache():
    """
    Main class for cache
    """
    def __init__(self):
        """ CONSTRUCTOR"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
        """  Get the values as specific func"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_int(self, data: int) -> int:
        """  Get the values as int" """
        try:
            int(data)
            return data
        except Exception:
            return 0

    def get_str(self, data: str) -> str:
        """  Get the values as str"""
        return self._redis.get(data).decode('utf_8')
