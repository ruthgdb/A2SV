class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        summ = 0
        minVal = float('-inf')
        for i in range(len(nums)):
            summ += nums[i]
            minVal = max(minVal, ceil(summ / (i+1)))
            
        return minVal
            