#!/usr/bin/python3
def write_file(filename="", text=""):
    import os
    with open(filename, "w+", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
