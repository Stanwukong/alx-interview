#!/usr/bin/python3
"""Rotates a 2D matrix."""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x m 2D matrix 90 degrees in
    place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
