#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    if isinstance(a_dictionary, dict):
        items = list(a_dictionary.values())
    else:
        items = a_dictionary
    total_salary = reduce(lambda acc, item: acc + item['salary'], items, 0)
    total_age = reduce(lambda acc, item: acc + item['age'], items, 0)
    avg_salary = total_salary / len(items)
    avg_age = total_age / len(items)
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
        f'The average salary is R${average_salary:.2f} '
        f'with an average age of {average_age}'
    )
