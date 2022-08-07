class Solution:
    def largestInteger(self, num: int) -> int:
        oddHeap, evenHeap, res = [], [], []
        
        for i, el in enumerate(str(num)):
            if int(el) % 2 == 0:
                evenHeap.append(-int(el))
            else:
                oddHeap.append(-int(el))
                
        heapq.heapify(evenHeap)
        heapq.heapify(oddHeap)
        
        for i, el in enumerate(str(num)):
            if int(el) % 2 == 0:
                temp = heapq.heappop(evenHeap)
                res.append(str(-temp))
            else:
                temp = heapq.heappop(oddHeap)
                res.append(str(-temp))
                
        return ''.join(res)