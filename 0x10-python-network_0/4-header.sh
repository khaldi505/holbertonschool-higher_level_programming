#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request
curl -sL -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
