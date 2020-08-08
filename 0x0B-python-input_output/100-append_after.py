#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding='utf-8') as my_file:
        lines = []
        for line in my_file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        my_file.seek(0)
        for line in lines:
            my_file.write(line)
