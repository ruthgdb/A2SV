class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def solve(nums):
            first = nums[0]
            second = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                third = max(second, first + nums[i])
                first = second
                second = third

            return second
            
        return max(solve(nums[1:]), solve(nums[:-1]))