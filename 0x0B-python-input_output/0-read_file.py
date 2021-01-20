#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file, prints to stdout"""
    with open(filename, encoding='utf-8') as f:
        for i in f:
            print(i, end="")
