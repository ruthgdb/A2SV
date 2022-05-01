class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def houses(i):
            if i >= len(nums):
                return 0
            
            if i not in memo:
                memo[i] = max(houses(i + 2), houses(i + 3)) + nums[i]
                
            return memo[i]
            
        return max(houses(0), houses(1))