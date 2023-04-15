class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def dp(i, k):
            if k == 0 or i == len(piles): 
                return 0
            
            maxCoins = dp(i + 1, k)
            currCoins = 0
            
            for j in range(min(len(piles[i]), k)):
                currCoins += piles[i][j]
                maxCoins = max(maxCoins, currCoins + dp(i + 1, k - j - 1))
                
            return maxCoins
        
        return dp(0, k)