# Lockboxes Project

## Description

The Lockboxes project is designed to solve a problem where you are given `n` locked boxes, each containing keys to other boxes. Your goal is to determine whether all the boxes can be unlocked starting from the first unlocked box (box 0). This problem can be modeled using graph traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS).

The function implemented in this project takes a list of lists as input, where each sublist represents a box and contains keys to other boxes. The function returns `True` if all boxes can be opened, otherwise `False`.

## Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
        boxes (list of list of int): List of lists where each list contains keys to other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

