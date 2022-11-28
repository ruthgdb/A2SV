# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        res = head.next
        prev = None
        curr = head
        nextt = head.next
        
        while nextt:
            if prev:
                prev.next = nextt
                
            curr.next = nextt.next
            nextt.next = curr
            prev = curr
            
            if not curr.next:
                break
                
            curr = curr.next
            nextt = curr.next
                
        return res