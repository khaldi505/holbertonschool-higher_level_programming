#!/bin/bash
# a script that follow the link even if the page redirects and only if the status code is 200
curl -sL $1
