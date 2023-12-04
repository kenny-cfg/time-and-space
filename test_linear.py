import time
import unittest

from linear import sum_of_integers


class Timer:
    def __enter__(self):
        self.start = time.process_time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.process_time()
        print(end - self.start)


class TestLinear(unittest.TestCase):
    def test_for_1000000_numbers(self):
        source = list(range(0, 1000000))
        sum_of_integers(source)

    def test_for_2000000_numbers(self):
        source = list(range(0, 2000000))
        sum_of_integers(source)

    def test_for_3000000_numbers(self):
        source = list(range(0, 3000000))
        sum_of_integers(source)


if __name__ == '__main__':
    unittest.main()
