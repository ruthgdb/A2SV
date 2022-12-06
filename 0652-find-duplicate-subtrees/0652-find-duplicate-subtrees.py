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
                return 'None'
            
            root = str(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            temp = root + ',' + left + ',' + right
            
            if duplicates[temp] == 1:
                res.append(node)
                
            duplicates[temp] += 1
            return temp
            
        dfs(root)
        return res