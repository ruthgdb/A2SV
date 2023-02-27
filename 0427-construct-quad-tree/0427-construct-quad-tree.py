"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node()
        n = len(grid)
         
        def checkSubMatrix(r1, c1, n):
            total = 0
            
            for r in range(r1, r1 + n):
                total += sum(grid[r][c1:c1 + n])
                
            return total == 0 or total == n ** 2
        
        def dfs(r1, c1, n, root):
            root.val = grid[r1][c1]
            
            if checkSubMatrix(r1, c1, n):
                root.isLeaf = True
            else:
                root.isLeaf = False
                root.topLeft = dfs(r1, c1, n // 2, Node())
                root.topRight = dfs(r1, c1 + (n // 2), n // 2, Node())
                root.bottomLeft = dfs(r1 + (n // 2), c1, n // 2, Node())
                root.bottomRight = dfs(r1 + (n // 2), c1 + (n // 2), n // 2, Node())
            
            return root
        
        return dfs(0, 0, n, root)