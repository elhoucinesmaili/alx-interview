#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    The rotation is performed by first transposing the matrix
    (swapping rows and columns) and then reversing each row.

    Args:
        matrix (list): A 2D list representing an n x n matrix

    Returns:
        None: The matrix is modified in-place
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
