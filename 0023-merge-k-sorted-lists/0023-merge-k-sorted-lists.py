# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode()
        dummy = res
        
        for i, lis in enumerate(lists):
            if lis:
                heapq.heappush(heap, (lis.val, i))
            
        while heap:
            temp = heapq.heappop(heap)
            dummy.next = lists[temp[1]]
            lists[temp[1]] = lists[temp[1]].next
            dummy = dummy.next
            if lists[temp[1]]:
                heapq.heappush(heap, (lists[temp[1]].val, temp[1]))
                
        return res.next