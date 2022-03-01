# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumN(root, s):
            if not root:
                return 0
            if not root.left and not root.right:
                s *= 10;
                s += root.val
                return s
            s *= 10;
            s += root.val
            return sumN(root.left, s) + sumN(root.right, s)
        
        return sumN(root, 0)
         