class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        noOfDecreasing = 0
        idx = -1
        
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                noOfDecreasing += 1
                idx = i
                
        if noOfDecreasing == 0:
            return True
        
        if noOfDecreasing == 1:
            if idx == 0 or idx == len(nums) - 1 or idx == len(nums) - 2:
                return True
            
            if nums[idx - 1] < nums[idx + 1] or nums[idx] < nums[idx + 2]:
                return True
            
        return False