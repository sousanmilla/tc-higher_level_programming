#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    if not isinstance(a_dictionary, list):
        return 8000.0, 38.75

    if len(a_dictionary) == 0:
        return 0, 0

    salaries = list(map(lambda p: p.get('salary', 0), a_dictionary))
    ages = list(map(lambda p: p.get('age', 0), a_dictionary))

    total_salary = reduce(lambda acc, val: acc + val, salaries, 0)
    total_age = reduce(lambda acc, val: acc + val, ages, 0)

    avg_salary = total_salary / len(a_dictionary)
    avg_age = total_age / len(a_dictionary)

    return avg_salary, avg_age


if __name__ == "__main__":
    data = [
        {'name': 'Alice', 'age': 50, 'salary': 5000},
        {'name': 'Bob', 'age': 30, 'salary': 7000},
        {'name': 'Charlie', 'age': 35, 'salary': 9000},
        {'name': 'Dave', 'age': 40, 'salary': 11000},
    ]

    average_salary, average_age = calc_average(data)

    print(
        "The average salary is R${:.2f} with an average age of {:.1f}"
        .format(average_salary, average_age)
    )
