#!/usr/bin/python3
def roman_to_int(roman_string):
    dic_roman = {
     'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
                }
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    total = 0
    prev_value = 0
    for i in reversed(roman_string):
        value = dic_roman.get(i, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
