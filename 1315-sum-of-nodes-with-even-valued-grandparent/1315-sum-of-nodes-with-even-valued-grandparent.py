# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(root):
            if not root:
                return 0

            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.total += root.left.left.val
                    if root.left.right:
                        self.total += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.total += root.right.left.val
                    if root.right.right:
                        self.total += root.right.right.val
        
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return self.total