# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxValue):
            if not node:
                return 0
            
            count = 0
            if node.val >= maxValue:
                count += 1
                
            count += dfs(node.left, max(node.val, maxValue))
            count += dfs(node.right, max(node.val, maxValue))
            
            return count
            
        return dfs(root, float("-inf"))