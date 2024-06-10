#!/usr/bin/env python3
'''
Module for concurrent coroutines.
'''

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    '''return the actual delay.'''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the delays in ascending order.'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert the delay in the correct position to maintain ascending order
        if not delays:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
            else:
                delays.append(delay)
    return delays
