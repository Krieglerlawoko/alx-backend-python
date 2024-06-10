#!/usr/bin/env python3
'''
Module for concurrent task coroutines.
'''

import asyncio
from typing import List
from task_wait_random import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawn task_wait_random n times and return
    the delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of delays in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
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
