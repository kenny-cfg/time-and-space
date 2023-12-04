import itertools
import unittest

from quadratic import substring_generator


class TestQuadratic(unittest.TestCase):
    def test_with_1000_string(self):
        substring_generator('a' * 1000)

    def test_with_2000_string(self):
        substring_generator('a' * 2000)

    def test_with_3000_string(self):
        substring_generator('a' * 3000)

    def test_with_4000_string(self):
        substring_generator('a' * 4000)

if __name__ == '__main__':
    unittest.main()
