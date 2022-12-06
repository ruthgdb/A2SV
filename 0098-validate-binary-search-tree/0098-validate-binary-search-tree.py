# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxValue, minValue):
            valid = False
            
            if minValue < node.val < maxValue:
                valid = True
                
            left = right = True
            
            if node.left:
                left = dfs(node.left, node.val, minValue)
            if node.right:
                right = dfs(node.right, maxValue, node.val)
                
            return left and right and valid
            
        return dfs(root, float("inf"), float("-inf"))