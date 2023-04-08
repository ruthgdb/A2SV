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
        
        newGraph = Node()
        newOld = {}
        visited = set()
        
        def build(root, node):
            root.val = node.val
            newOld[node.val] = root
            
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    newNei = Node()
                    root.neighbors.append(newNei)
                    build(newNei, nei)
                else:
                    root.neighbors.append(newOld[nei.val])
            
        visited.add(node)
        build(newGraph, node)
        return newGraph