#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async function that collects and returns random numbers """
    # async for that yields each number into list
    return [x async for x in async_generator()]
