# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = list1
        temp2 = list2
        merged = ListNode(0)
        head = merged

        while temp and temp2:
            if temp.val < temp2.val:
                merged.next = temp
                temp = temp.next
            else:
                merged.next = temp2
                temp2 = temp2.next
            merged = merged.next
        
        if not temp:
            merged.next = temp2
        else:
            merged.next = temp
            
        return head.next
    