# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numberOfNodes(self, root): 
        if not root:
            return 0
        
        return self.numberOfNodes(root.left) + self.numberOfNodes(root.right) + 1
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.numberOfNodes(root)