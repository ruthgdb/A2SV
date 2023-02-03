# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        grid, res = defaultdict(list), []
        mini, maxx = float(inf), float(-inf)
        
        def dfs(node, i, j):
            nonlocal mini, maxx
            mini, maxx = min(mini, j), max(maxx, j)
            grid[j].append((i, node.val))
            if node.left: dfs(node.left, i + 1, j - 1)
            if node.right: dfs(node.right, i + 1, j + 1)
         
        dfs(root, 0, 0)
        
        for i in range(mini, maxx + 1):
            temp = sorted(grid[i])
            res.append([x[1] for x in temp])
            
        return res
    