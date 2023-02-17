# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minDiff = float("inf")
        
        def dfs(root):
            nonlocal minDiff
            left = dfs(root.left) if root.left else (float("inf"), float("inf"))
            right = dfs(root.right) if root.right else (float("inf"), float("inf"))
            minDiff = min(minDiff, abs(root.val - left[1]), right[0] - root.val)
            
            # min, max
            return (left[0] if left[0] != float("inf") else root.val, right[1] if right[1] != float("inf") else root.val)
           
        dfs(root)    
        return minDiff