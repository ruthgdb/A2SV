# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        
        def traverse(node):
            if not node:
                return 0
            
            nonlocal maxSum
            
            left = 0
            right = 0
            
            if node.left:
                left = max(left, traverse(node.left))
                
            if node.right:
                right = max(right, traverse(node.right))
             
            maxSum = max(maxSum, node.val + left + right)
            return max(left + node.val, right + node.val)
        
        traverse(root)
        return maxSum