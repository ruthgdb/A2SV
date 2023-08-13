class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dp(i):
            if i == len(nums):
                return True
            
            if i >= len(nums) - 1:
                return False
            
            two_equals = three_equals = three_inc = False
            
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    two_equals = dp(i + 2)
                    
            if i < len(nums) - 2:
                if nums[i] == nums[i + 1] == nums[i + 2]:
                    three_equals = dp(i + 3)
                    
                if nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2:
                    three_inc = dp(i + 3)
            
            return two_equals or three_equals or three_inc
        
        return dp(0)