class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        subarrays = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
            else:
                subarrays += (count * (count + 1)) // 2
                count = 0
            
        subarrays += (count * (count + 1)) // 2
        return subarrays