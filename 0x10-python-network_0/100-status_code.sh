#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL
curl -so /dev/null --write-out "%{http_code}" "$1"
