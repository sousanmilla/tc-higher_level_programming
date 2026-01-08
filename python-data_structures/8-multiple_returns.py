#!/usr/bin/python3

def multiple_returns(frase):
    return (len(frase), frase[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
