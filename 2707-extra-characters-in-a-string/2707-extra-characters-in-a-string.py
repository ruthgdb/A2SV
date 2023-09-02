class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        
        @cache
        def dp(i):
            if i == len(s):
                return 0

            min_count = dp(i + 1) + 1
            
            for j in range(i, len(s)):
                curr = s[i: j + 1]
                if curr in dictionary:
                    min_count = min(min_count, dp(j + 1))
                    
            return min_count
            
        return dp(0)