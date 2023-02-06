class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longestChain = 1
        words.sort(key=len)
        dp = defaultdict(int)
        
        for i, word in enumerate(words):
            currChain = 1
            
            for j in range(len(word)):
                preWord = word[:j] + word[j + 1:]
                if preWord in dp:
                    currChain = max(currChain, dp[preWord] + 1)
            
            longestChain = max(longestChain, currChain)
            dp[word] = max(dp[word], currChain)
            
        return longestChain