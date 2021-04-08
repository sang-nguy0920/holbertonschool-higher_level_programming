#!/bin/bash
# Bash script that takes in a URL, sends and displays
curl -w '%{size_download}\n' -so /dev/null $1
