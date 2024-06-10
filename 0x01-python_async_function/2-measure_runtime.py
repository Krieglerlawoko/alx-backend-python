#!/usr/bin/env python3
'''
Module to measure runtime of wait_n.
'''

import asyncio
import time
from typing import Tuple
from 1_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure total execution time for wait_n(n, max_delay)

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay value.

    Returns:
        float: Average time per call.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
