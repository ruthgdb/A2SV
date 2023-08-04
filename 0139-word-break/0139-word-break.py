class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @cache
        def dp(i):
            if i >= len(s):
                return True
            
            found = False
            
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    found |= dp(j + 1)
                    
            return found
                    
        return dp(0)