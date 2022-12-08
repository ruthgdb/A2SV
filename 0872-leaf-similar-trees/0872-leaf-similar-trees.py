# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        firstLeaves = []
        secondLeaves = []
        
        def dfs(node, tree):
            if not node:
                return
            
            if not node.left and not node.right:
                if tree == 'first':
                    firstLeaves.append(node.val)
                else:
                    secondLeaves.append(node.val)
                    
            dfs(node.left, tree)
            dfs(node.right, tree)
            
        dfs(root1, 'first')
        dfs(root2, 'second')
        return firstLeaves == secondLeaves