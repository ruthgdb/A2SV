# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        sumNodePairs = {}
        prefSum = 0
        
        '''
        [1,2,3,-3,4]
         1 3 6 3
        '''
        
        while head:
            prefSum += head.val
            
            if prefSum == 0:
                dummy = head.next
                sumNodePairs.clear()
            elif prefSum in sumNodePairs:
                curr = sumNodePairs[prefSum]
                # print(curr, prefSum, head)
                temp = head.next
                total = prefSum
                curr = curr.next

                while curr != head:
                    total += curr.val
                    del sumNodePairs[total]
                    curr = curr.next

                head = sumNodePairs[prefSum]
                head.next = temp
            else:    
                sumNodePairs[prefSum] = head
            head = head.next
            
        return dummy