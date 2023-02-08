class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            mini, idx = float(inf), i + 1
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums) and dp[j] < mini:  mini, idx = dp[j], j
                    
            dp[i] = 1 + dp[idx]
            
        return dp[0]