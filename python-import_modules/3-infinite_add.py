#!/usr/bin/python3
import sys


def main():

    args = sys.argv[1:]
    total = 0
    for valor in args:
        total += int(valor)
    print(total)


if __name__ == "__main__":
    main()
