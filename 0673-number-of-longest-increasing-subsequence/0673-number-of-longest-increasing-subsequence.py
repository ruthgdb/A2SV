class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        max_len = 1
        res = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = 0
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                max_len = max(max_len, dp[i])
            
        for i in range(len(nums)):
            if dp[i] == max_len:
                res += count[i]
             
        return res