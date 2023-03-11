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
    def findMiddle(self, head):
        slow = head
        prev = None
        fast = head.next
        found = False
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            found = True
        
        return (slow, found) if not found else (prev, found)
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def buildBST(node):
            if not node:
                return None
            
            if not node.next:
                return TreeNode(node.val)
            
            prev, found = self.findMiddle(node) 
            mid = prev.next
            right = buildBST(mid.next)
            prev.next = None
            left = buildBST(node) if found else TreeNode(node.val)
            newNode = TreeNode(mid.val)
            if left:
                newNode.left = left
            if right:
                newNode.right = right
            
            return newNode
        
        return buildBST(head)