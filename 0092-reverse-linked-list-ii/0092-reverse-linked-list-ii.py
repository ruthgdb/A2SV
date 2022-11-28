# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head
        count = 0
        last = None
        
        for _ in range(left - 1):
            last = head
            head = head.next
        
        first = head
        prev = head
        curr = head
        nextt = curr.next
        prev.next = None
        
        while nextt and count < (right - left):
            curr = nextt
            nextt = curr.next
            curr.next = prev
            prev = curr
            count += 1
        
        first.next = nextt
        
        if last: 
            last.next = prev
            return dummy
            
        return curr