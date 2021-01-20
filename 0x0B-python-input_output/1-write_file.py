#!/usr/bin/python3
"""Inits"""


def write_file(filename="", text=""):
    """writes a string to a text file, returns the number of characters written"""
    num = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        num += f.write(text)
        f.close()
    return num
