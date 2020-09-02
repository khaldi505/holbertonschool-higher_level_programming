#!/usr/bin
# post a jason file and see if it's valid
curl -s -X POST --data @"$2" "$1"
