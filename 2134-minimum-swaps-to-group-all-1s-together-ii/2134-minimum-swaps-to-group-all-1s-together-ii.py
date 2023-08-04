class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # checking if not circular
        ones_count = nums.count(1)
        zeros = 0
        left = 0
        min_swaps = float("inf")
        
        for right in range(len(nums)):
            zeros += nums[right] == 0
            
            if right - left + 1 > ones_count:
                zeros -= nums[left] == 0
                left += 1
                
            if right - left + 1 == ones_count:
                min_swaps = min(min_swaps, zeros)
                
        # checking if circular
        zeros_count = len(nums) - ones_count
        ones = 0
        left = 0
        
        for right in range(len(nums)):
            ones += nums[right] == 1
            
            if right - left + 1 > zeros_count:
                ones -= nums[left] == 1
                left += 1
                
            if right - left + 1 == zeros_count:
                min_swaps = min(min_swaps, ones)
                
        return min_swaps