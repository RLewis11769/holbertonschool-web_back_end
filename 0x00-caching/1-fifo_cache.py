#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements FIFO cache """

    def __init__(self):
        """ Override cache_data as OrderedDict not dict """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put method to assign item value to key and delete first-in """
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                # popitem deletes and returns dict at first index (in this case)
                k, v = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(k))

    def get(self, key):
        """ Get method to return value at key """
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
