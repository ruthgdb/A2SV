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
            left = dfs(node.left)
            # print(left, dfs(node.left))
            right = dfs(node.right)
            
            path = path + left
            path = path + right
            # print(node.val, left, right)
            temp = tuple(path)
            # print(node, left, right)
            if duplicates[temp] == 1:
                # print(node, left, right)
                res.append(node)
                
            duplicates[temp] += 1
            return path
            
        dfs(root)
        # print(duplicates)
        return res