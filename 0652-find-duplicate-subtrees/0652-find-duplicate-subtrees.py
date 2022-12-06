# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = defaultdict(int)
        res = []
        
        def dfs(node):
            if not node:
                return [None]
            
            path = [node.val]
            path = path + dfs(node.left)
            path = path + dfs(node.right)
            temp = tuple(path)
            
            if duplicates[temp] == 1:
                res.append(node)
                
            duplicates[temp] += 1
            return path
            
        dfs(root)
        return res