#!/usr/bin/env python3
""" Type-annotated function """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function that multiplies float by multiplier """
    def multiply_by_multiplier(num: float) -> float:
        """ Return the product of multiplier and value """
        return multiplier * num
    return multiply_by_multiplier
