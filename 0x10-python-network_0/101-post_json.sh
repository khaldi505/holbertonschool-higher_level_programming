#!/bin/bash
# post a jason file and see if it's valid
curl -s -X POST --data @"$2" -H "Content-Type: application/json" "$1"
