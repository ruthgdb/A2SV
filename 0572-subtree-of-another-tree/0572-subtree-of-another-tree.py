# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validateSubTree(self, node, subNode):
        if not node and not subNode:
            return True
        
        if not node or not subNode:
            return False
        
        root = left = right = False
        root = node.val == subNode.val
        left = self.validateSubTree(node.left, subNode.left)
        right = self.validateSubTree(node.right, subNode.right)
        return root and left and right
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isValid = False
        
        def dfs(node):
            nonlocal isValid
            
            if node.val == subRoot.val:
                isValid = isValid or self.validateSubTree(node, subRoot)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)
            
        dfs(root)
        return isValid