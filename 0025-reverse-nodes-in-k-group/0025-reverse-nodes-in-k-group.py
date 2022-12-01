# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def checkIfValid(self, left, k):
            right = left
            count = 0
            
            while right:
                right = right.next
                count += 1
                if count == k - 1:
                    return right
            
            return None
        
    def reverse(self, node, k):
            if k == 1:
                return node
                
            newHead = self.reverse(node.next, k - 1)
            node.next.next = node
            node.next = None
            
            return newHead
                
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = ListNode(0)
        dummy = curr
        left = head
        
        while left:
            nextt = left
            right = self.checkIfValid(left, k)
            
            if not right:
                curr.next = nextt
                return dummy.next
            else:
                right = right.next
                temp = self.reverse(left, k)
                curr.next = temp
                
                for _ in range(k):
                    curr = curr.next
           
                left = right
                
        return dummy.next