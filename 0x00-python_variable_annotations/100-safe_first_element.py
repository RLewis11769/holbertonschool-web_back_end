#!/usr/bin/env python3
""" Type-annotated function """


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns first element of list if list exists """
    """ First element can be any type but can also return nothing """
    if lst:
        return lst[0]
    else:
        return None
