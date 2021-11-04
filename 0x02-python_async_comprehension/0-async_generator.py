#!/usr/bin/env python3
""" Type-annotated asynchronous coroutine """
from random import uniform
from time import sleep

async def async_generator():
	""" Async function that waits 1 second then yields random number 10 times """
	for x in range(10):
		sleep(1)
		yield uniform(1, 10)
