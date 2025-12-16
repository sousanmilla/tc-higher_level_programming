#!/usr/bin/python3
import sys


def main():

    n = len(sys.argv) - 1
    args = sys.argv[1:]

    if n == 1:
        print("{} argument:".format(n))
    elif n == 0:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))

    if n > 0:
        for i in range(len(args)):
            print("{}: {}".format(i + 1, args[i]))


if __name__ == "__main__":
    main()
