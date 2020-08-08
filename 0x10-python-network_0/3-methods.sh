#!/bin/bash
# URL and D.
curl -sI 0.0.0.0:5000/route_4 -i | grep "Allow:"|cut -d ' ' -f2-
