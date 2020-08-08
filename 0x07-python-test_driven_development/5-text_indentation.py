#!/usr/bin/python3
""" function that add a text indentation. """


def text_indentation(text):
    """
    text = str
    """
    txt = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for y in range(len(text)):
        if text[y] == " " and text[y - 1] in [".", "?", ":"]:
                txt += ""
        else:
            txt += text[y]
    for x in range(len(txt)):
        if txt[x] in [".", "?", ":"]:
                print(txt[x])
                print()
        else:
            print(txt[x], end="")
