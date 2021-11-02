#!/usr/bin/env python3
""" Type-annotated function """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns key/value pair as tuple where value is squared """
    return (k, v * v)
