# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, node):
        slow = node
        fast = node.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        return slow
    
    def merge(self, node1, node2):
        newList = ListNode(0)
        dummy = newList
        first = node1
        second = node2
        
        while first and second:
            if first.val < second.val:
                newList.val = first.val
                first = first.next
            else:
                newList.val = second.val
                second = second.next
                
            if first and second:
                newList.next = ListNode(0)
                newList = newList.next
                
        if first:
            newList.next = first
        
        if second:
            newList.next = second
            
        return dummy
        
        return newList
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.findMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)