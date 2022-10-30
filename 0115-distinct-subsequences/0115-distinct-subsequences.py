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
                top_left = dp[i - 1][j - 1] if i > 0 and j > 0 else 1
                left = dp[i][j - 1] if j > 0 else 0
                
                if t[i] == s[j]:
                    dp[i][j] = left + top_left
                else:
                    dp[i][j] = left
        
        
        return dp[-1][-1]