#!/usr/bin/python3
"""Paschal's triangle."""


def pascal_triangle(n):
    """Generate a Pascal Triangle of size n.
    Args:
        n (int): Size of the Pascal Triangle.
    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)
        triangle.append(row)

    return triangle
