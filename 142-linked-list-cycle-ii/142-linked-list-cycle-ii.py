# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPtr = head
        slowPtr = head
        
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
            if slowPtr == fastPtr:
                while slowPtr != head:
                    head = head.next
                    slowPtr = slowPtr.next
                return slowPtr
            
        return None