# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, lis):
        if not lis or not lis.next:
            return lis
        
        prev = None
        curr = lis
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)
        
        carry = 0
        first = l1
        second = l2
        res = ListNode()
        head = res
        
        while first or second:
            res.val = carry
            
            if first:
                res.val += first.val
                first = first.next
            if second:
                res.val += second.val
                second = second.next
                
            if res.val >= 10:
                carry = 1
                res.val = res.val % 10
            else:
                carry = 0
                
            if first or second:
                res.next = ListNode()
                res = res.next
                
        if carry:
            res.next = ListNode()
            res = res.next
            res.val = carry
            
        head = self.reverseLL(head)
        return head