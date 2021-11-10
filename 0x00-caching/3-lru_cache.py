#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements LIFO cache """

    def __init__(self):
        """ Init new instance variable as OrderedDict instead of dict """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put method to assign item value to key """
        if (key and item):
            # Assign value and move data to end of dict
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > self.MAX_ITEMS:
                # popitem returns first or last with last as default
                # So set last=False to choose first
                discard = self.cache_data.popitem(last=False)
                print('Discard: {}'.format(discard[0]))

    def get(self, key):
        """ Get method to return value at key """
        # if key not in self.cache_data:
        #     return None
        if key and key in self.cache_data:
            # if access key, more recently used so move to end
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
