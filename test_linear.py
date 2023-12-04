import unittest

from linear import sum_of_integers


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
