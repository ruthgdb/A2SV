class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n  
        
        mod = 10 ** 9 + 7
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        
        for i in range(3, n):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]

        return dp[-1] % mod