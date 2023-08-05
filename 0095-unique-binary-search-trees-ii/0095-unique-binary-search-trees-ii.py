# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dp(i, j):
            if i > j:
                return [None]
            
            res = []
            
            for k in range(i, j + 1):
                lefts = dp(i, k - 1)
                rights = dp(k + 1, j)
                
                for l in lefts:
                    for r in rights:
                        node = TreeNode(k, l, r)
                        res.append(node)
                        
            return res
        
        return dp(1, n)