class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # the virst value is for increasing and the second for decreasing
        increasing_dp = 1
        decreasing_dp = 1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                increasing_dp = decreasing_dp + 1
            elif nums[i] < nums[i + 1]:
                decreasing_dp = increasing_dp + 1

        return max(increasing_dp, decreasing_dp)