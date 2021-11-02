#!/usr/bin/env python3
""" Type-annotated function """


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return the length of an element in tuple with updated annotations """
    return [(i, len(i)) for i in lst]
