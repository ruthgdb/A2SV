# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        leftMost = [-1, 0]
        
        def dfs(node, level):
            if not node:
                return
            
            if not node.left and not node.right:
                if leftMost[0] < level:
                    leftMost[0] = level
                    leftMost[1] = node.val
                    
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return leftMost[1]