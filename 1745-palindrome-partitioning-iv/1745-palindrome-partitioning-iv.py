class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        palindroms = defaultdict(list)
        dp = [[False, False, False, False] for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(n):
            left, right = i, i
            
            while left >= 0 and right < n and s[left] == s[right]:
                palindroms[left].append(right + 1)
                left -= 1
                right += 1
                    
            left, right = i, i + 1
            
            while left >= 0 and right < n and s[left] == s[right]:
                palindroms[left].append(right + 1)
                left -= 1
                right += 1
         
        for i in range(n):
            for j in palindroms[i]:
                dp[j][1] |= dp[i][0] 
                dp[j][2] |= dp[i][1]
                dp[j][3] |= dp[i][2]
                
        return dp[-1][3]