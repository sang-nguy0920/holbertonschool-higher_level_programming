#!/usr/bin/python3
""" Function that reads a text file (UTF8) and prints it to stdout: """


def read_file(filename=""):
    """ read_file method:
        Args:
            filename = name of file(string)
        Returns:
            None
    """
    with open(filename, encoding='utf-8') as f:
        for x in f:
            print(x, end="")
