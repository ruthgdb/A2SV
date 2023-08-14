# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete_vals = set(to_delete)
        
        def dfs(node, is_root):
            if not node:
                return 
            
            if is_root:
                res.append(node)
                    
            if node.val not in to_delete_vals:
                dfs(node.left, False)
                dfs(node.right, False)
            else:
                if node.left:
                    dfs(node.left, node.left.val not in to_delete_vals)
                if node.right:
                    dfs(node.right, node.right.val not in to_delete_vals)

            if node.left and node.left.val in to_delete_vals:
                node.left = None

            if node.right and node.right.val in to_delete_vals:
                node.right = None

        dfs(root, root.val not in to_delete_vals)
        return res