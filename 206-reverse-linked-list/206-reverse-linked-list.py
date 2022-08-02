# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        ptr1 = head
        head = head.next  
        ptr1.next = None
        
        while head != None:
            ptr2 = head.next
            head.next = ptr1
            ptr1 = head
            head = ptr2
            
        return ptr1