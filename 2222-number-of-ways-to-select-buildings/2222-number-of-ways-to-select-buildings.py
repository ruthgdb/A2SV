class Solution:
    def numberOfWays(self, s: str) -> int:
        #0, 1, 01, 10, 010, 101
        dp = [0] * 6
        
        for i in range(len(s)):
            if s[i] != '0':
                dp[3] += dp[1]
                dp[4] += dp[2]
                dp[0] += 1
            else:
                dp[2] += dp[0]
                dp[5] += dp[3]
                dp[1] += 1
            
        return dp[-1] + dp[-2]