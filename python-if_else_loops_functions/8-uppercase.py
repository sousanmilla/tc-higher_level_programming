#!/usr/bin/python3
s = input("digite:")
def uppercase(str):
    result = ""
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            result += chr(char_code - 32)
        else:
            result += char
    print(result)
(uppercase("{}".format(s)))
