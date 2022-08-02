# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        temp = head
        
        while(temp.next != None):
            length += 1
            temp = temp.next
        
        mid = (length // 2) + 1
        length = 1
        
        while(length < mid):
            length += 1
            head = head.next
            
        return head