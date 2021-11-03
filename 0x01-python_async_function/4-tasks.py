#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function that calls task_wait_random n number of times """
    # task_list holds coroutine objects holding floats
    task_list: List = []
    # complete_list holds floats
    complete_list: List[float] = []

    for x in range(n):
        # task_wait_random asyncronously starts each task
        task_list.append(task_wait_random(max_delay))
    # As each task is completed, it's waited for and then appended
    # wait is just a coroutine object containing float
    for task in asyncio.as_completed(task_list):
        completed: float = await task
        # Now completed can be accessed - this can't be one line
        complete_list.append(completed)

    return (complete_list)
