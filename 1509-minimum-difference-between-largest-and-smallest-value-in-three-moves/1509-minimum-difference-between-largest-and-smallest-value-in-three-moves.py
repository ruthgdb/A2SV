class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
        -10, 0, 2, 5, 8, 10, 12, 20
        
        len = 6
        windiw size = 6 - 3 = 3
        min_diff = 30
        if len <= 3: 0
        
        left = 0, right = 2, min_diff = 12
        left = 1, right = 3, min_diff = 10
        left = 2, right = 4, min_diff = 10
        left = 3, right = 5, min_diff = 10
        
        TC: O(n log n), n = len(nums)
        SC: O(1)
        
        '''
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        window_size = len(nums) - 3
        left = 0
        min_diff = nums[-1] - nums[0]
        
        for right in range(len(nums)):
            if right - left + 1 > window_size:
                left += 1
                
            if right - left + 1 == window_size:
                min_diff = min(min_diff, nums[right] - nums[left])
                
        return min_diff