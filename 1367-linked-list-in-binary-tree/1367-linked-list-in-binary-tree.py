# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validateLinkedList(self, node, head):
        if not head:
            return True
        
        if not node:
            return False
 
        if head.val == node.val:
            left = self.validateLinkedList(node.left, head.next)
            right = self.validateLinkedList(node.right, head.next)
            return left or right
        
        return False

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        isValid = False
        
        def dfs(node):
            nonlocal isValid
            
            if node.val == head.val:
                isValid = isValid or self.validateLinkedList(node, head)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)
        return isValid