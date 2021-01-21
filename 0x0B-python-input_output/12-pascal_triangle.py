#!/usr/bin/python3
"""
the triangle of Pascal
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    prev = [1]
    row = 0
    if n <= 0:
        return []
    triangle.append(prev)
    if n == 1:
        return triangle
    while row < n - 1:
        current = []
        current.append(prev[0])
        x = 0
        while x < row:
            current.append(prev[x] + prev[x + 1])
            x += 1
        current.append(prev[len(prev) - 1])
        triangle.append(current)
        prev = current
        row += 1
    return triangle
