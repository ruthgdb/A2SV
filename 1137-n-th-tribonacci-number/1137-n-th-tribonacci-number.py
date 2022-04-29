class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n < 3:
            return 1
        
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            
        return dp[-1] + dp[-2] + dp[-3]