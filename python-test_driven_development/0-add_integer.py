#!/usr/bin/python3
"""
O módulo contem a função add_integer.
Que retorna o inteiro da soma de dois valores.
"""


def add_integer(a, b=98):
    """A função retorna um número inteiro, a soma de a e b."""
    def _invalid_float(x):
        return isinstance(x, float) and (x != x or x == float(
            'inf') or x == float('-inf'))

    if not isinstance(a, (int, float)) or _invalid_float(a):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or _invalid_float(b):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
