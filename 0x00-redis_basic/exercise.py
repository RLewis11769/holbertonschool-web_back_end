#!/usr/bin/env python3
""" File to hold exercises to get more familiar with Redis """
from functools import wraps
from typing import Callable, Union
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """
    Counts the number of times a method is called
    Returns method with count newly attached

    Args:
        method: method that is wrapped and counted
    """

    @wraps(method)
    def wrapper(self, *args):
        """
        Define wrapper to increment counter on each call

        Args:
            self: instance itself, so can access Redis instance
            value: uh
        """
        # Qualname defines specific method
        # Can differentiate between methods with same name based on location
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


class Cache():
    """ Class to cache info in a Redis database """

    def __init__(self):
        """ Initialize Redis database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in key:value pair in Redis database
        Return randomly-generated key associated with given data

        Args:
            data: data to store in Redis database, could be any data type
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """
        Convert data to desired format and return it
        Conserve original Redis.get behavior if function not passed

        Args:
            key: key to retrieve data from Redis database
            fn: optional function to call if data is not in Redis database
        """
        if fn:
            # If string, essentially cast with str(key)
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        Return data in string format

        Args:
            key: key to cast as string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Return data in int format

        Args:
            key: key to cast as int
        """
        return self.get(key, int)
