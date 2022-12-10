# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        vals = []
        mod = 10 ** 9 + 7
        
        def dfs(node): 
            if not node: return 0 
            ans = node.val + dfs(node.left) + dfs(node.right)
            vals.append(ans)
            return ans
        
        total = dfs(root)
        return max((total-x) * x for x in vals) % mod