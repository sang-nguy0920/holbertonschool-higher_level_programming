#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
