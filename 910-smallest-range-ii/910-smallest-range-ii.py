class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = nums[-1] - nums[0]
        maximum = nums[-1] - k
        minimum = nums[0] + k

        for i in range(len(nums) - 1):
            left = min(minimum, nums[i+1] - k)
            right = max(maximum, nums[i] + k)

            result = min(result, right - left)
    
            
        return result