class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo1 = {}
        memo2 = {}
        
        def withoutFirst(i):
            if i >= len(nums):
                return 0
            
            if i not in memo1:
                memo1[i] = max(withoutFirst(i + 1), withoutFirst(i + 2) + nums[i])
            
            return memo1[i]
        
        def withoutLast(i):    
            if i >= len(nums) - 1:
                return 0
            
            if i not in memo2:
                memo2[i] = max(withoutLast(i + 1), withoutLast(i + 2) + nums[i])
            
            return memo2[i]         
        
        
        return max(withoutFirst(1), withoutLast(0))