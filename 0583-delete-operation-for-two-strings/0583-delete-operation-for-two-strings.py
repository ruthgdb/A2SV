class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)
            
            skip_both = float("inf")
            
            if word1[i] == word2[j]:
                skip_both = dp(i + 1, j + 1)
                
            delete_first = dp(i + 1, j) + 1
            delete_second = dp(i, j + 1) + 1
            
            return min(skip_both, delete_first, delete_second)
        
        return dp(0, 0)