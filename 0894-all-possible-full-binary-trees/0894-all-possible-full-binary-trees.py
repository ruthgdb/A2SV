# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        @cache
        def dfs(idx):
            if idx == 1:
                return [(TreeNode(), 1)]
            
            res = dfs(idx - 2)
            temp = []
            
            for node1, i in res:
                for node2, j in res:
                    if i + j == idx - 1:
                        new_node = TreeNode()
                        new_node.left = node1
                        new_node.right = node2
                        temp.append((new_node, idx))
              
            res.extend(temp)
            return res
              
        res = dfs(n)
        return [node for node, i in res if i == n]