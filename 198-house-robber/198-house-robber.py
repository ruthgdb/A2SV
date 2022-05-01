class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            house1 = dp[i + 2] if i + 2 < n else 0
            house2 = dp[i + 3] if i + 3 < n else 0
            dp[i] = max(house1, house2) + nums[i]
            
        return max(dp[0], dp[1])