#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sLi "$1" | curl "Allow" | awk "{print $2}"
