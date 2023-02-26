class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dp(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            minCost = float("inf")
            
            if word1[i] == word2[j]:
                minCost = dp(i + 1, j + 1)
            else:
                insert = dp(i, j + 1)
                delete = dp(i + 1, j)
                update = dp(i + 1, j + 1)
                
                minCost = min(insert, update, delete) + 1
             
            memo[(i, j)] = minCost
            return minCost
        
        return dp(0, 0)