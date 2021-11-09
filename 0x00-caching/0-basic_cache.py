#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements cache """

    def put(self, key, item):
        """ Put method to assign item value to key """
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """ Get method to return value at key """
        if key:
            return self.cache_data.get(key)
