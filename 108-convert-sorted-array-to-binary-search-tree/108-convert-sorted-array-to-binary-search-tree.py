# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(lis):
            if not lis:
                return None
           
            mid = len(lis) // 2
            root = TreeNode(lis[mid])
            root.left, root.right = makeBST(lis[:mid]), makeBST(lis[mid + 1:])
            return root
         
        return makeBST(nums)