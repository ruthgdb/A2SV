# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node, robbed):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return node.val if not robbed else 0
                                            
            rob = 0
            notRob = dfs(node.left, False) + dfs(node.right, False)
            
            if not robbed:
                rob = node.val + dfs(node.left, True) + dfs(node.right, True)
            
            return max(rob, notRob)
           
        return max(dfs(root, False), dfs(root, True))