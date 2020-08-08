#!/usr/bin/python3
"""test """
def read_lines(filename="", nb_lines=0):
    """test """
    with open(filename, encoding="utf-8") as my_file:
        text = my_file.readlines()
        if nb_lines <= 0:
            for y in range(len(text)):
                    print("{}".format(text[y]), end="")
            print()
        if nb_lines >= len(text):
            for a in range(len(text)):
                print("{}".format(text[a]), end="")
            print()
        else:
            for x in range(nb_lines):
                print("{}".format(text[x]), end="")
