#!/usr/bin/env python3
"""async_comprehension that takes no arguments"""

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions  """
    n = [i async for i in async_generator()]
    return n
