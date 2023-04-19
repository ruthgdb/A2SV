# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLength = [0]
        
        def dp(node, prev, currLength):
            maxLength[0] = max(maxLength[0], currLength)
            
            if prev == 'L':
                if node.left:
                    dp(node.left, 'R', currLength + 1)
                if node.right:
                    dp(node.right, 'L', 1)
            else:
                if node.right:
                    dp(node.right, 'L', currLength + 1)
                if node.left:
                    dp(node.left, 'R', 1)
            
        dp(root, "R", 0)
        dp(root, "L", 0)
        return maxLength[0]