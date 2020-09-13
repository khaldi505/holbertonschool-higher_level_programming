#!/usr/bin/python3
"""
using the requests package to
read the X-request-id in the response header
"""


def go_go_power_rangers():

    import requests
    from sys import argv
    req = requests.get(argv[1])
    print(r.headers["X-Request-Id"])


if __name__ == "__main__":
    go_go_power_rangers()
