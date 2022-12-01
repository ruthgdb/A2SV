# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return 
        
        dummy = head
        slow = head
        fast = head.next
        last = ListNode()
        res = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
              
        prev = slow.next
        slow.next = None
        curr = prev.next
        prev.next = None
        
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
          
        while prev and dummy:
            nextt = dummy.next
            dummy.next = prev
            temp = prev.next
            prev.next = nextt
            dummy = nextt
            prev = temp
                    