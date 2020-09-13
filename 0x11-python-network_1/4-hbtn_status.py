#!/usr/bin/python3
"""
using the requests package to
read the body response
"""


def go_go_power_rangers():

    import requests
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:  {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    go_go_power_rangers()
