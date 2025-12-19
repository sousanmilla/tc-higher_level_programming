#!/usr/bin/python3
import hidden_4


def main():

    nomes = dir(hidden_4)
    nomes_fil = [n for n in nomes if not n.startswith("__")]
    for nome in sorted(nomes_fil):
        print("{}".format(nome))

if __name__ == "__main__":
    main()
