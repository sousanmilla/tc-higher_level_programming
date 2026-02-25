#!/usr/bin/python3
"""
Esse módulo contem uma função para divisão de um amatriz por um número inteiro.
"""


def matrix_divided(matrix, div):
    """Conferindo que a matrix é uma lista de listas."""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists)"
            " of integers/floats"
        )
    """Conferindo que as linhas da matrix tem o mesmo tamanho."""
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    """Conferindo que a matrix só contem números."""
    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )
    """Conferindo que div é um número."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """Conferindo que div não é zero."""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round((i / div), 2) for i in r] for r in matrix]
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
