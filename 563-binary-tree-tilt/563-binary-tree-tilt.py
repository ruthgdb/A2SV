# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, total=0):
        self.total = total
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def rootSums(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            return root.val + rootSums(root.left) + rootSums(root.right)
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        self.total += abs(rootSums(root.left) - rootSums(root.right))
        self.findTilt(root.left) 
        self.findTilt(root.right)
        
        return self.total
        
        