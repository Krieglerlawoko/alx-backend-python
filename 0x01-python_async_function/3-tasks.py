#!/usr/bin/env python3
'''
Module for creating asyncio tasks.
'''

import asyncio
from typing import List
from random import uniform


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Return an asyncio.

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: An asyncio Task object.
    '''
    async def wait_random():
        delay = uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay
    return asyncio.create_task(wait_random())
