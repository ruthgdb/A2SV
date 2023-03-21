class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        currMax = 0
        right = currMax
        count = 0
        
        while right < len(nums) - 1:
            currMax = 0
            while left <= right:
                currMax = max(currMax, left + nums[left])
                left += 1
            
            right = currMax
            count += 1
            
        return count