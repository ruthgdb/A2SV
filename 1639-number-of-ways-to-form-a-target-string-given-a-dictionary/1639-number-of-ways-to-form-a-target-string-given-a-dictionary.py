class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        chars = defaultdict(int)
        
        for word in words:
            for i, char in enumerate(word):
                chars[(i, char)] += 1
                
        @cache
        def dp(i, j):
            if j == len(target):
                return 1
            
            if i >= len(words[0]):
                return 0
          
            count = dp(i + 1, j) + chars[(i,target[j])] * dp(i + 1,j + 1)
            return count % mod
                
        return dp(0, 0) % mod