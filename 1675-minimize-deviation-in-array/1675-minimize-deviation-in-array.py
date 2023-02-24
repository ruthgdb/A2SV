class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        1 3 4 5 20
        2 3 4 5 5
        '''
        
        heap = []
        res = float('inf')
        
        for num in nums:
            if num % 2 == 0:
                num = -num
            else:
                num = -num * 2
            heapq.heappush(heap, num)
            
        minn = -max(heap)

        while len(nums) == len(heap):
            curr = -heapq.heappop(heap)
            res = min(res, curr- minn)
            
            if curr % 2 == 0:
                minn = min(minn, curr//2)
                heapq.heappush(heap, -curr//2)
            else:
                break
        
        return res