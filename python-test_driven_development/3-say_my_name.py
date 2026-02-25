#!/usr/bin/python3
"""
Este módulo contem uma função para dizer o nome e o sobrenome enviado
previamente.
"""


def say_my_name(first_name, last_name=""):
    """Conferindo se o nome é string."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    """Conferindo se o sobrenome é string."""
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}$".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
