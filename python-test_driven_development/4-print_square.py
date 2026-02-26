#!/usr/bin/python3
"""
Este módulo contem uma função para imprimir quadrados.
"""


def print_square(size):
    """Conferindo que size é um número inteiro."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    """Conferindo que size é um número maior que zero."""
    if size < 0:
        raise ValueError("size must be >= 0")
    """Conferindo que size não é um número float nem menor que zero."""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    """Impriminto um quadrado."""
    for i in range(size):
        print(size*"#")


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
