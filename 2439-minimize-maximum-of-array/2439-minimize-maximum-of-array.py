class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        minMax = 0
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            minMax = max(minMax, math.ceil(total/(i + 1)))
            
        return minMax