# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        currSum = 0

        if low <= root.val <= high:
            currSum += root.val

        currSum += self.rangeSumBST(root.left, low, high)   
        currSum += self.rangeSumBST(root.right, low, high)

        return currSum
