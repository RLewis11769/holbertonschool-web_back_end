#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Retrieves dict of rows based on index given """
        """ Deletion-resistent meaning can delete data and still get output """
        assert (type(index) is int and index < len(self.__indexed_dataset))
        # index is current start index of first item on current page
        # Next page is index of first item after last item on current page
        next = index + page_size
        # Query dataset with next index to retrieve data
        data = self.dataset()[index: next]
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next
        }
