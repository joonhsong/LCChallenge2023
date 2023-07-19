"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copied = {}
        def dcopy(node):
            if node in copied:
                return copied[node]
            cop = Node(node.val)
            copied[node] = cop
            for n in node.neighbors:
                cop.neighbors.append(dcopy(n))
            return cop
        return dcopy(node)
        