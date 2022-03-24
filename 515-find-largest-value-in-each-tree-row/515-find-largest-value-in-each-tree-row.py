# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return 
        
        queue = deque([root])
        length = 1
        level = []
        res = []
        
        while queue:
            level = []
            temp = 0
            for i in range(length):
                temp2 = queue.popleft()
                level.append(temp2.val)
                if temp2.left:
                    queue.append(temp2.left)
                    temp += 1
                if temp2.right:
                    queue.append(temp2.right)
                    temp += 1
            length = temp
            res.append(max(level))
            
        return res