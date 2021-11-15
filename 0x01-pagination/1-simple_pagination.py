#!/usr/bin/env python3
""" Helper function for pagination files """
import csv
import math
from typing import List, Tuple, Union


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieve list of rows based on page and page_size """
        # Data verification
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        # Retrieve necessary data (data and range needed)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        # Verify input arguments are in available range for dataset
        if (end > len(dataset)):
            return []
        # Add data from page to list to return
        pageList = []
        for page in range(start, end):
            pageList.append(dataset[page])
        return pageList
