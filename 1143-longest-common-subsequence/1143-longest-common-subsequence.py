class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
                        
            if text1[i] == text2[j]:
                length = 1 + dp(i + 1, j + 1)
            else:
                length = max(dp(i, j + 1), dp(i + 1, j))
                
            return length
            
        
        return dp(0, 0)