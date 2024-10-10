#!/usr/bin/python3
"""Determines if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): List where each index represents a box
        and contains a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    visited = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
