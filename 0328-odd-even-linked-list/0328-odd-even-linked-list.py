# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        oddDummy = odd
        evenDummy = even
        
        while (odd and odd.next) or (even and even.next):
            if odd and odd.next:
                odd.next = odd.next.next
                if odd.next:
                    odd = odd.next
            if even and even.next:
                even.next = even.next.next
                even = even.next
            
        odd.next = evenDummy
        return oddDummy