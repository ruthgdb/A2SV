class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * len(s)
        
        '''
        applepenapple
        fffftfft
        
        '''
        
        for i in range(len(s)):
            found = s[:i + 1] in wordDict
            
            if not found:
                for j in range(i):
                    if dp[j] and s[j + 1:i+ 1] in wordDict:
                        found = True
                        break
                        
            dp[i] = found
                    
        return dp[-1]