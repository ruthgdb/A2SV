# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini, maxx = float(-inf), float(inf)
        
        def dfs(node, mini, maxx):
            if not node:
                return True
            
            if node.val <= mini or node.val >= maxx:
                return False
            
            return dfs(node.left, mini, node.val) and dfs(node.right, node.val, maxx)
            
        return dfs(root, mini, maxx)