#!/usr/bin/python3
"""
using the requests package to
read the X-request-id in the response header
"""


def go_go_power_rangers():

    import requests
    from sys import argv
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)


if __name__ == "__main__":
    go_go_power_rangers()
