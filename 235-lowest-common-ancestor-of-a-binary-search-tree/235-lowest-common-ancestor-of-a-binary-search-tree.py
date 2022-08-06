# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val:
            if q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        else:
            if q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root