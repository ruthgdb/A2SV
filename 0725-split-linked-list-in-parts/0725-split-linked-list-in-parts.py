# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        i = 0
        dummy = head
        lis = [None for _ in range(k)]
        res = [lis[i] for i in range(k)]
        
        # count length of linkedlist
        while dummy:
            n += 1
            dummy = dummy.next
        
        # find the size of each partition and the remaining nodes left
        size = n // k
        left = n % k
        count = size + 1 if left > 0 else size
        left -= 1
        
        dummy = head
        
        while dummy:
            if not lis[i]:
                lis[i] = dummy
                res[i] = dummy
            
            count -= 1
            
            # if current partition is finished, start a new partition at next index
            if count == 0:
                temp = dummy.next
                dummy.next = None
                dummy = temp
                count = size + 1 if left > 0 else size
                left -= 1
                i += 1
            else:
                lis[i] = lis[i].next    
                dummy = dummy.next
              
        return res