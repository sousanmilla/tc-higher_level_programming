#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    salaries = [item['salary'] for item in a_dictionary]
    ages = [item['age'] for item in a_dictionary]
    somas = reduce(lambda x, y: x + y, salaries, 0)
    somaa = reduce(lambda x, y: x + y, ages, 0)
    n = len(a_dictionary)
    return somas / n, somaa / n


if __name__ == "__main__":
    data = [
        {'name': 'Alice', 'age': 50, 'salary': 5000},
        {'name': 'Bob', 'age': 30, 'salary': 7000},
        {'name': 'Charlie', 'age': 35, 'salary': 9000},
        {'name': 'Dave', 'age': 40, 'salary': 11000},
    ]

    average_salary, average_age = calc_average(data)

    print(
        f'The average salary is R${average_salary:.2f} '
        f'with an average age of {average_age}'
    )
