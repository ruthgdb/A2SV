# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path = []
        
    def findPath(self, node, target, currPath):
        if not node:
            return
        
        if node.val == target.val:
            self.path = currPath[:]
            return
        
        if node.left:
            self.findPath(node.left, target, currPath + ['L'])
            
        if node.right:
            self.findPath(node.right, target, currPath + ['R'])
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.findPath(root, target, [])
        nodes = []
        
        def dfs(node, dist, idx):
            nonlocal k
            if dist == k:
                nodes.append(node.val)
               
            if 0 <= idx < len(self.path):
                if node.left:
                    if self.path[idx] == 'L':
                        dfs(node.left, dist - 1, idx + 1)
                    else:
                        dfs(node.left, dist + 1, float("inf"))
                        
                if node.right:
                    if self.path[idx] == 'R':
                        dfs(node.right, dist - 1, idx + 1)
                    else:
                        dfs(node.right, dist + 1, float("inf"))
                
            else:
                if node.left:
                    dfs(node.left, dist + 1, idx)
                
                if node.right:
                    dfs(node.right, dist + 1, idx)
                
            
        dfs(root, len(self.path), 0)
        return nodes