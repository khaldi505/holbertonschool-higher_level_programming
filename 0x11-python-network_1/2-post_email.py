#!/usr/bin/python3
# post an email on a website
from urllib import request, parse
from sys import argv as argv
def go_go_power_rangers():
	email = parse.urlencode({"email": argv[2]})
	email = email.encode("ascii")
	url = argv[1]
	with request.urlopen(url, email) as rep:
	    info = rep.read()
	print(info.decode("UTF-8"))
if __name__ == "__main__":
    go_go_power_rangers()
