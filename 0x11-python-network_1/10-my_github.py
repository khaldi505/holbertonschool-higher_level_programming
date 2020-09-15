#!/usr/bin/python3
"""
using the requests package """


def go_go_power_rangers():
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    req = requests.get(
        "https://api.github.com/user/{}".format(argv[1]),
        auth=HTTPBasicAuth(argv[1], argv[2]))
    req = req.json()
    print(req.get("id"))


if __name__ == "__main__":
    go_go_power_rangers()
