#!/usr/bin/python3
for i in range(1, 50):
    if i > 9 and i < 12 or i > 19 and i < 23 or i > 29 and i < 34:
        continue
    print("{:02d}, ".format(i), end="")
for i in range(45, 79):
    if i > 59 and i < 67 or i > 69 and i < 78:
        continue
    print("{:02d}, ".format(i), end="")
print(89)
