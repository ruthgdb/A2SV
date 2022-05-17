# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = None
        
        def dfs(org, clone):  
            nonlocal res
            if org:
                if org == target:
                    res = clone

                dfs(org.left, clone.left)
                dfs(org.right, clone.right)
            
        dfs(original, cloned)
        return res