#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request
curl -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
