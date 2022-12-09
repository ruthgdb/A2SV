# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0
        
        def dfs(node, maxValue, minValue):
            nonlocal maxDiff
            
            if not node:
                return 
            
            maxDiff = max(maxDiff, abs(maxValue - node.val), abs(minValue - node.val))
            dfs(node.left, max(maxValue, node.val), min(minValue, node.val))
            dfs(node.right, max(maxValue, node.val), min(minValue, node.val))
            
        dfs(root, root.val, root.val)
        return maxDiff