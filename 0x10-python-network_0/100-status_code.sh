#!/bin/bash
# status code
curl -si 0.0.0.0:5000 | grep HTTP/1.0 | awk '{ print $2}'
