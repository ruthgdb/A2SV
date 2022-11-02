class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        increasing_dp = 1
        decreasing_dp = 1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                increasing_dp = decreasing_dp + 1
                decreasing_dp = decreasing_dp
            elif nums[i] < nums[i + 1]:
                decreasing_dp = increasing_dp + 1
                increasing_dp = increasing_dp
            
        return max(increasing_dp, decreasing_dp)