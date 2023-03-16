# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {inorder[i]:i for i in range(len(inorder))}
        
        def dfs(l, r, postorder):
            if l == r:
                return None
            
            n = postorder.pop()
            root = TreeNode(n)
            root.right = dfs(hashmap[n] + 1, r, postorder)
            root.left = dfs(l, hashmap[n], postorder)
            return root
        
        return dfs(0, len(inorder), postorder)