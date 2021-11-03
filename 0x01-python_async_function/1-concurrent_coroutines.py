#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """
# import asyncio
# from random import uniform
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function that waits random time between 0 and max_delay """
    # wait_list holds coroutine objects holding floats
    wait_list: List = []
    # complete_list holds floats
    complete_list: List[float] = []

    for x in range(n):
        # wait_random asyncronously starts tasks
        wait_list.append(asyncio.create_task(wait_random(max_delay)))
    # As each task is completed, it's waited for and then appended
    # wait is just a coroutine object containing float
    for wait in asyncio.as_completed(wait_list):
        completed: float = await wait
        # Now completed can be accessed - this can't be one line
        complete_list.append(completed)

    return (complete_list)
