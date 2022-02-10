# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            stack.append(slowPtr.val)
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
        if fastPtr:
            slowPtr = slowPtr.next
            
        while slowPtr:
            if not slowPtr.val == stack.pop():
                return False
            else:
                slowPtr = slowPtr.next
            
        return True