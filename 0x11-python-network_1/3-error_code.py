#!/usr/bin/python3
"""
prints the error status code
"""


def go_go_power_rangers():

    from urllib import request, error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as req:
            data = req.read()
            print(data.decode("UTF-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    go_go_power_rangers()
