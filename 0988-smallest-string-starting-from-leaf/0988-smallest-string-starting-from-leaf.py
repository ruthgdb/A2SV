# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, path):
            if not node:
                return '|'
            
            char = chr(97 + node.val)
            path += char
            
            if not node.left and not node.right:
                return path[::-1]
            
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            
            return min(left, right)
        
        return dfs(root, '')
        