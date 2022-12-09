# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        res = 0
        
        def dfs(node, total):
            nonlocal res, targetSum
            if not node:
                return 0
            
            total += node.val
            
            if total - targetSum in sums:
                res += sums[total - targetSum]
                
            sums[total] += 1
                
            dfs(node.left, total)
            dfs(node.right, total)
            
            sums[total] -= 1
                        
        dfs(root, 0)
        return res