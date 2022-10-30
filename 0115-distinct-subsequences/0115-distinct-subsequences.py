class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        - if letters are equal: check if valid was found before at i-1, j-1
        - if found: take number at i-1, j-1 and add i, j - 1
        - if not found: take i, j - 1
        - if i = 0: add 1 if letters are equal
        
        """
        
        dp = []
        
        for _ in range(len(t)):
            dp.append([0] * len(s))
            
        for i in range(len(t)):
            for j in range(i, len(s)):
                if s[j] == t[i]:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                        # print(s[i], t[j], i, j, dp[i][j])
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1] + 1
                    elif j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] if j > 0 else 0
            # print(dp[i])
        
        return dp[-1][-1]