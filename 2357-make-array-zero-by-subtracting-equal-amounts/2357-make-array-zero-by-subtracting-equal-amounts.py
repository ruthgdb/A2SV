class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heapq.heapify(nums)
        
        while nums:
            temp = heapq.heappop(nums)
            
            if temp != 0:
                count += 1
                for i in range(len(nums)):
                    nums[i] -= temp
                    
        return count