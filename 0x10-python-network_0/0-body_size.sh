#!/bin/bash
# this script will give you the content length per bytes
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
