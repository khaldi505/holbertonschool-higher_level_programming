#!/usr/bin/python3

""" sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
from sys import argv


def go_go_power_rangers():

    with urllib.request.urlopen(argv[1]) as response:
        req = response.info()
        print("{}".format(req["X-Request-Id"]))

if __name__ == "__main__":
    go_go_power_rangers()
