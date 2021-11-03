#!/usr/bin/env python3
""" Type-annotated function """


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Takes in tuple and returns list """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Pass in tuple
array = (12, 72, 91)

zoom_2x = zoom_array(array)
# print(zoom_2x) # Uncomment to test output

# Factor needs to be int because must be iterable for range
zoom_3x = zoom_array(array, 3)
