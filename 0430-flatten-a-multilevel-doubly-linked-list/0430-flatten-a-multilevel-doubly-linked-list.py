"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flattenNodes(self, right, head):
            temp = head.next
            head.next = head.child
            head.child.prev = head
            head.child = None
            right.next = temp
            if temp:
                temp.prev = right
            head = right.next
            
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        
        def traverse(node):
            curr = node
            prev = None
            
            while curr:
                if curr.child:
                    right = traverse(curr.child)
                    self.flattenNodes(right, curr)
                prev = curr
                curr = curr.next
            
            return prev
        
        traverse(head)
        return dummy