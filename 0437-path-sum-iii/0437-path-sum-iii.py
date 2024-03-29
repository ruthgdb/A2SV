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
        
        def dfs(node, total, targetSum):
            if not node:
                return 0
            
            currSum = 0
            total += node.val
            
            if total - targetSum in sums:
                currSum += sums[total - targetSum]
                
            sums[total] += 1
                
            currSum += dfs(node.left, total, targetSum) + dfs(node.right, total, targetSum)
            
            sums[total] -= 1
            return currSum 
        
        return dfs(root, 0, targetSum)