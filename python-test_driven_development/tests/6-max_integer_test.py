#!/usr/bin/python3
import unittest


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


if __name__ == "__main__":
    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertTrue(max_integer([1, 2, 3, 4]) == 4)

    def test_max_in_middle(self):
        self.assertTrue(max_integer([1, 3, 4, 2]) == 4)

    def test_max_at_beginning(self):
        self.assertTrue(max_integer([4, 3, 1, 2]) == 4)

    def test_one_negative_number(self):
        self.assertTrue(max_integer([1, -3, 2, 4]) == 4)

    def test_only_negative_numbers(self):
        self.assertTrue(max_integer([-1, -3, -4, -2]) == -1)

    def test_one_element(self):
        self.assertTrue(max_integer([4]) == 4)

    def test_list_is_empty(self):
        self.assertTrue(max_integer() is None)
