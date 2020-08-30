#!/bin/bash
# post a parameters
curl -s -X POST "$1" -d email="hr@holbertonschool.com" -d subject="I will always be here for PLD"
