#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    salaries = [item['salary'] for item in a_dictionary]
    ages = [item['age'] for item in a_dictionary]
    somas = reduce(lambda x, y: x + y, salaries, 0)
    somaa = reduce(lambda x, y: x + y, ages, 0)
    n = len(a_dictionary)
    return somas / n, somaa / n
