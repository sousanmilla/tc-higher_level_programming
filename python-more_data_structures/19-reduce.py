#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    if not isinstance(a_dictionary, list) or (a_dictionary and not isinstance(a_dictionary[0], dict)):
        raise TypeError("calc_average(a_dictionary): 'a_dictionary' deve ser list[dict].")

    n = len(a_dictionary)
    if n == 0:
        return 0.0, 0.0

    meds, medi = reduce(
        lambda acc, r: (acc[0] + r['salary'], acc[1] + r['age']),
        a_dictionary,
        (0.0, 0.0)
        )
    return meds / n, medi / n


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
