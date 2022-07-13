class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = nums[i] if dp[i - 1] < 0 else dp[i - 1] + nums[i]
                
        return max(dp)