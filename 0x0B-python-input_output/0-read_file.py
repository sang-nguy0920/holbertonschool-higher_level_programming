#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file, prints to stdout"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
        a_file.close()
