"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        oldtonew={}
        q=deque()
        q.append(node)
        start=node
        # visited=set()
        while q:
            node= q.popleft()
            oldtonew[node]=Node(node.val)
            for neighbour in node.neighbors:
                if neighbour not in oldtonew:
                    q.append(neighbour)

        for old_node,new_node in oldtonew.items():
            for neighbour in old_node.neighbors:
                new_node.neighbors.append(oldtonew[neighbour])

        return oldtonew[start]