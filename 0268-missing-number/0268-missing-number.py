class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        
        for i in range(len(nums)):
            missing ^= nums[i]
            missing ^= i
            
        return missing ^ len(nums)