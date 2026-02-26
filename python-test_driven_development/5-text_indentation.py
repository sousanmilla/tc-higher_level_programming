#!/usr/bin/python3
"""
Imprimindo um texto com duas novas linhas após cada um desses caracteres:
'.', '?' e ':'.
"""


def text_indentation(text):
    """Conferindo que text é uma string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """Removendo o espaço do início ou do final de cada linha impressa."""
    cleaned = ""
    prev_space = False
    for ch in text:
        if ch == " ":
            if not prev_space:
                cleaned += " "
            prev_space = True
        else:
            cleaned += ch
            prev_space = False
    new_line = True
    for char in cleaned:
        if new_line and char == " ":
            continue

        print(char, end="")
        new_line = False

        if char in ".?:":
            print("\n")
            new_line = True


if __name__ == "__main__":
    text_indentation(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? \
        Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. \
        Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis? \
        Teneo, inquit, finem illi videri nihil dolere. \
        Transfer idem ad modestiam vel temperantiam, \
        quae est moderatio cupiditatum \
        rationi oboediens. Si id dicis, vicimus. \
        Inde sermone vario sex illa a Dipylo \
        stadia confecimus. Sin aliud quid voles, \
        postea. Quae animi affectio suum \
        cuique tribuens atque hanc, quam dico. \
        Utinam quidem dicerent alium alio \
        beatiorem! Iam ruinas videres"""
    )
