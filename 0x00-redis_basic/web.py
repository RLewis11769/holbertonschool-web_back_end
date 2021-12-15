#!/usr/bin/env python3
""" File to hold exercises to get more familiar with Redis """
from functools import wraps
from typing import Callable
import redis
import requests


def count_calls(method: Callable) -> Callable:
    """
    Returns method with count of calls added to key "count:{url}"
    Counts number of times method is called
    Adds expiration time in seconds to key

    Args:
        method: method to wrap and add count/key expiration to
    """
    local_redis = redis.Redis()

    @wraps(method)
    def wrapper(*args):
        """
        Defines wrapper to count number of calls and sets expiration time
        Returns value of wrapped method

        Args:
            *args: method's arguments - args[0] is url for get_page(url)
        """
        key = f"count:{args[0]}"
        local_redis.incr(key)
        local_redis.set(key)
        local_redis.expire(key, 10)
        return method(*args)
    return (wrapper)


@count_calls
def get_page(url: str) -> str:
    """ Return HTML content for given URL """
    content = requests.get(url)
    return content.text
