class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindroms = defaultdict(list)
        minCut = float("inf")
        dp = [float("inf")] * (n + 1)
        dp[0] = -1
        
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
                dp[j] = min(dp[j], dp[i] + 1)
        
        return dp[-1]