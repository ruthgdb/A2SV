# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, float("-inf"))
            
            left, left_max = dfs(node.left)
            right, right_max = dfs(node.right)
            curr_max = node.val
            if left > 0:
                curr_max += left
                
            if right > 0:
                curr_max += right
                
            return (max(left, right, 0) + node.val, max(curr_max, left_max, right_max))
        
        return dfs(root)[1]