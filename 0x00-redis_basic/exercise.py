#!/usr/bin/env python3
""" File to hold exercises to get more familiar with Redis """
from typing import Union
from uuid import uuid4
import redis

class Cache():
    """ Class to cache info in a Redis database """

    def __init__(self):
        """ Initialize Redis database """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
