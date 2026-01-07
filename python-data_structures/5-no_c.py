#!/usr/bin/python3

def no_c(my_string):
    resultado = str.maketrans({"c": None, "C": None})
    return my_string.translate(resultado)


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
