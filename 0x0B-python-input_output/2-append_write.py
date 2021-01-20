#!/usr/bin/python3
"""
function that appends a string at the end of a text
file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string"""
    with open(filename, mode='a', encoding='utf-8') as f:
        num = f.write(text)
    return num
