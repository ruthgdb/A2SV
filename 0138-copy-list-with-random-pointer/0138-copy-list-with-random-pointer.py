"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        dummy = head
        newPtrs = {}
        newRandoms = {}
        newList = Node(0)
        res = newList
        
        while head:
            newList.val = head.val
            newPtrs[head] = newList
            newRandoms[newList] = head.random

            if head.next:
                newList.next = Node(0)
                newList = newList.next
                
            head = head.next
            
        newList = res
        head = dummy
 
        while newList:            
            if head.random:
                temp = newPtrs[head.random]
                newList.random = temp
                
            newList = newList.next  
            head = head.next
            
        return res