# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 0)])
        level = 0
        last = False
        
        while queue:
            if last:
                return False
            
            if len(queue) != 2 ** level:
                last = True
            
            j = 0
            prev = -1
            
            for _ in range(len(queue)):
                curr, i = queue.popleft()
                prev += 1
                
                if prev != i:
                    return False
                
                if curr.left:
                    queue.append((curr.left, j))
                
                if curr.right:
                    queue.append((curr.right, j + 1))
                
                j += 2
                    
            level += 1
            
        return True