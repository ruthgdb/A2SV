# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        def build(node, nums):
            maxNum = max(nums)
            idx = -1
            
            for i in range(len(nums)):
                if nums[i] == maxNum:
                    idx = i
                    
            node.val = maxNum
            left = nums[:idx]
            right = nums[idx + 1:]
            
            if left:
                node.left = TreeNode()
                build(node.left, left)
            if right:
                node.right = TreeNode()
                build(node.right, right)
            
        build(root, nums)
        return root