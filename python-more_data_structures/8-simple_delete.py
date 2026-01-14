#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))


if __name__ == "__main__":
    a_dictionary = {
        'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]
    }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
