#!/usr/bin/env python3
""" Type-annotated function """


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ lst is any sequence that is iterable """
    """ Return is list of tuples with first idx sequenceable and second int """
    """ Returns list of lengths of element at each index of tuple """
    return [(i, len(i)) for i in lst]
