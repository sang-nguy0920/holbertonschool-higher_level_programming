#!/usr/bin/python3
for lower in range(122, 96, -1):
    if lower % 2 == 0:
        print("{:c}".format(lower), end="")
    else:
        print("{:c}".format(lower - 32), end="")
