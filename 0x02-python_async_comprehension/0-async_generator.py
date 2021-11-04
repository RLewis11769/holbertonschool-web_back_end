#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """

from random import uniform
from asyncio import sleep
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ Async function that waits 1 second then yields random num 10 times """
    for x in range(10):
        # Asyncio sleep is non-blocking while time sleep is blocking
        await sleep(1)
        yield uniform(1, 10)
