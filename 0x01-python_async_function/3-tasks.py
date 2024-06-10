#!/usr/bin/env python3
'''
Module to create asyncio tasks.
'''

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Returns an asyncio.

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: An asyncio Task object.
    '''
    return asyncio.create_task(wait_random(max_delay))
