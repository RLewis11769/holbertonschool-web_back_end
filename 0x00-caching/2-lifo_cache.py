#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements LIFO cache """

    def __init__(self):
        """ Init new instance variable and keep any orig variables """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ Put method to assign item value to key and delete last-in """
        if (key and item):
            self.cache_data[key] = item
            # List contains all keys found in dict in order
            if key not in self.cache_list:
                self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                # pop deletes and returns key at index
                discarded = self.cache_list.pop(self.MAX_ITEMS - 1)
                print('DISCARD: {}'.format(discarded))
                del self.cache_data[discarded]

    def get(self, key):
        """ Get method to return value at key """
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
