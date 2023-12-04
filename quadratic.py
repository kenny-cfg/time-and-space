# Write a function that takes a string
# and outputs all two character strings where each character
# is a character of the original string
#
# e.g. f('ab') should give ['aa', 'ab', 'ba', 'bb']
#
# Work out the time complexity of this function
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
def substring_generator(source: str) -> List[str]:
    result = []
    for first_character in source:
        for second_character in source:
            result.append(f'{first_character}{second_character}')
    return result
