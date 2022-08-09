# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        queue, res = deque(), []
        
        queue.append(root)
        res.append(root.val)
        
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            
            if queue:
                res.append(queue[-1].val)
                
        return res