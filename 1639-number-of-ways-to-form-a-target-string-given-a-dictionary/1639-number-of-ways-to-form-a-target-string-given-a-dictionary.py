class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        chars = [defaultdict(int) for _ in range(len(words[0]))]
        
        for i in range(len(words[0])):
            for j in range(len(words)):
                chars[i][words[j][i]] += 1
                
        @cache
        def dp(i, j):
            if j == len(target):
                return 1
            
            if i >= len(words[0]):
                return 0
          
            count = (dp(i + 1, j) + (chars[i][target[j]] * dp(i + 1, j + 1))) % mod

            return count
                
        return dp(0, 0) % mod