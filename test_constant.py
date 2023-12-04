import unittest

from constant import take_first_element


class ConstantTest(unittest.TestCase):
    def test_single_element_list(self):
        take_first_element([50])

    def test_multiple_elements(self):
        source_list = list(range(0, 10000))
        take_first_element(source_list)


if __name__ == '__main__':
    unittest.main()
