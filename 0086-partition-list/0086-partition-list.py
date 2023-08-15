# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        res = ListNode()
        dummy = res
        first = head
        
        while first:
            if first.val < x:
                res.next = ListNode(first.val)
                res = res.next
                
            first = first.next
        
        second = head
        
        while second:
            if second.val >= x:
                res.next = ListNode(second.val)
                res = res.next
                
            second = second.next
            
        return dummy.next