#!/usr/bin/env python3

import asyncio
from random import uniform


async def wait_random(max_delay=10):
    random = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
