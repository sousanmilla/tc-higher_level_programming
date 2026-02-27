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
    def test_max_no_fim(self):
        self.assertTrue(max_integer([1, 2, 3, 4]) == 4)

    def test_max_no_meio(self):
        self.assertTrue(max_integer([1, 3, 4, 2]) == 4)

    def test_max_no_inicio(self):
        self.assertTrue(max_integer([4, 3, 1, 2]) == 4)

    def test_max_tudo_igual(self):
        self.assertTrue(max_integer([4, 4, 4, 4]) == 4)

    def test_max_tudo_igual(self):
        self.assertTrue(max_integer([4, 4, 4, 4]) == 4)

    def test_max_tudo_negativo(self):
        self.assertTrue(max_integer([-1, -3, -4, -2]) == -1)

    def test_max_so_um(self):
        self.assertTrue(max_integer([4]) == 4)

    def test_vazio(self):
        self.assertTrue(max_integer() is None)


if __name__ == '__main__':
    unittest.main()
