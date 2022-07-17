class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] < 0:
                return abs(nums[i])
            nums[val] *= -1