from typing import List


def sum_of_integers(source: List[int]) -> int:
    sum_so_far = 0
    for x in source:
        sum_so_far += x
    return sum_so_far
