#!/usr/bin/env python3
""" Type-annotated function """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums every float in list and returns float """
    return sum(input_list)
