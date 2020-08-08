#!/usr/bin/python3
import os
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
