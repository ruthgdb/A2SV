# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def reverse(node):
            if not node or not node.next:
                return node
                
            newHead = reverse(node.next)
            node.next.next = node
            node.next = None
            
            return newHead
        
        return reverse(head)