#!/usr/bin/env python3
""" Type-annotated function """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums every float/int in list and returns float """
    return sum(mxd_lst)
