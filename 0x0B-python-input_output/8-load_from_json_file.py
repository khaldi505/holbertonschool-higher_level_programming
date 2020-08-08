#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename) as My_file:
        text = My_file.read()
        return json.loads(text)
