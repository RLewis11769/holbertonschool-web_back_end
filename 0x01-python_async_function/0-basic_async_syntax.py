#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """
import asyncio
from random import uniform
from typing import Optional


async def wait_random(max_delay: int = 10) -> float:
    """ Async function that waits random time between 0 and max_delay """
    random: float = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
