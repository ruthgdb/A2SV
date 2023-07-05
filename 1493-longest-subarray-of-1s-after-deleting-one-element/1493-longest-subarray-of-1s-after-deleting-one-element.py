class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            zeros += nums[right] == 0
            
            while zeros > 1:
                zeros -= nums[left] == 0
                left += 1
                
            max_len = max(max_len, right - left)
            
        return max_len