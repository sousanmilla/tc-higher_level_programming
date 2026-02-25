#!/usr/bin/python3
"""
O módulo contem a função add_integer.
Que retorna o inteiro da soma de dois valores.
E contem um arquivo de texto para teste nesse mesmo diretorio
"""


def add_integer(a, b=98):
    """
    A função retorna um número inteiro, a soma de a e b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    def to_int(x, which):
        if isinstance(x, float):
            if x != x:
                raise ValueError("cannot convert float NaN to integer")
            if x == float('inf') or x == float('-inf'):
                raise OverflowError("cannot convert float infinity to integer")
        return int(x)

    return to_int(a, "a") + to_int(b, "b")


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
