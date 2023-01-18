class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSubarray = maxSubarray = maxSum = minSum = nums[0]
        total = sum(nums)
        
        for i in range(1, len(nums)):
            minSubarray = min(nums[i], minSubarray + nums[i])
            minSum = min(minSum, minSubarray)
            maxSubarray = max(nums[i], maxSubarray + nums[i])
            maxSum = max(maxSum, maxSubarray)
       
        return max(total - minSum, maxSum) if total != minSum else maxSum