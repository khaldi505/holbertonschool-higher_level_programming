#!/usr/bin/python3
"""
using the requests package to
read the X-request-id in the response header
"""


def go_go_power_rangers():
    import requests
    from sys import argv
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        jsobj = req.json()
        if not bool(jsobj):
            print("No result")
            return
        print("[{}] {}".format(jsobj["id"], jsobj["name"]))
    except ValueError as e:
        print("Not a valid JSON")
        return


if __name__ == "__main__":
    go_go_power_rangers()
