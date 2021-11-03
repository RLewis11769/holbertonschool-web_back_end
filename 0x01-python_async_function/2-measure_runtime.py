#!/usr/bin/env python3
""" Type-annotated function that measures time of asynchronous coroutine """
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures time where wait_n is being run """
    start = time()
    # Run starts tasks, runs until complete, and finishes
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
