#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    integers = list_of_integers
    length = len(integers)
    if length == 0:
        return
