class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * n
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[-1] + dp[-2]