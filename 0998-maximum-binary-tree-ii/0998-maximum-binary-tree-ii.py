# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        
        def build(parent, curr):
            if curr.val < val:
                node = TreeNode(val)
                parent.right = node
                node.left = curr
                
            else:
                if curr.right:
                    build(curr, curr.right)
                else:
                    node = TreeNode(val)
                    curr.right = node
                            
        build(None, root)
        return root
    