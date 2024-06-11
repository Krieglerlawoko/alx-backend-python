#!/usr/bin/env python3
"""async_comprehension"""


from 0_async_generator import async_generator

async def async_comprehension():
    """Collect 10 random numbers from async_generator and return them."""
    return [i async for i in async_generator()]
