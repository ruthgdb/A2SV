class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            
            if i == len(s1):
                return sum([ord(s2[l]) for l in range(j, len(s2))])
            
            if j == len(s2):
                return sum([ord(s1[l]) for l in range(i, len(s1))])
            
            skip_both = float("inf")
            
            if s1[i] == s2[j]:
                skip_both = dp(i + 1, j + 1)
                
            delete_first = dp(i + 1, j) + ord(s1[i])
            delete_second = dp(i, j + 1) + ord(s2[j])
            
            return min(skip_both, delete_first, delete_second)
        
        return dp(0, 0)