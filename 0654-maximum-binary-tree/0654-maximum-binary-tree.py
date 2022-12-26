# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        root = None
        
        for num in nums:
            temp = None
            curr = TreeNode(num)
            
            while stack and stack[-1].val < num:
                if not temp:
                    temp = stack.pop()
                else:
                    popped = stack.pop()
                    popped.right = temp
                    temp = popped
                    
            stack.append(curr)
            curr.left = temp
            
        while stack:
            if not root:
                root = stack.pop()
            
            else:
                curr = stack.pop()
                curr.right = root
                root = curr
                
        return root
            
        