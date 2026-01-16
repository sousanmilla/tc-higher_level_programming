#!/usr/bin/python3

from functools import reduce


def calc_average(a_dictionary):
    n = len(a_dictionary)
    if n == 0:
        return 0.0, 0.0

    meds, medi = reduce(
        lambda acc, r: (acc[0] + r['salary'], acc[1] + r['age']),
        a_dictionary,
        (0.0, 0.0)
        )
    return meds / n, medi / n
