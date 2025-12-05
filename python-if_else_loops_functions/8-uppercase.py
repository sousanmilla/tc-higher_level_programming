#!/usr/bin/python3
p = "holberton"
def uppercase(str):
    result = ""
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            result += chr(char_code - 32)
        else:
            result += char
    return result
print("{}".format(uppercase(p)))
