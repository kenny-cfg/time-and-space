import time
from typing import List


def timer(func):
    def inner(*args, **kwargs):
        start = time.process_time()
        func(*args, **kwargs)
        end = time.process_time()
        print(end - start)
    return inner


@timer
def sum_of_integers(source: List[int]) -> int:
    sum_so_far = 0
    for x in source:
        sum_so_far += x
    return sum_so_far
