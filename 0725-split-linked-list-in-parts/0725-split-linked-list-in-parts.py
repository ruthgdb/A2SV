# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        dummy = head
        lis = [ListNode(-1) for _ in range(k)]
        ans = [lis[i] for i in range(k)]
        
        while dummy:
            n += 1
            dummy = dummy.next
            
        size = n // k
        left = n % k
        i = 0 
        count = size
        
        if left > 0:
            count += 1
            left -= 1
            
        dummy = head
        
        while dummy:
            lis[i].next = ListNode(dummy.val)
            lis[i] = lis[i].next
            count -= 1
            
            if count == 0:
                count = size
                if left > 0:
                    count += 1
                    left -= 1
                i += 1
                
            dummy = dummy.next
            
        for i in range(len(ans)):
                ans[i] = ans[i].next
                
        return ans