class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache
        def dp(i, count):
            if i >= len(piles):
                return 0
            
            val = 0
            
            for x in range(1, (2 * count) + 1):
                val = max(val, sum(piles[i:]) - dp(i + x, max(x, count))) 
                      
            return val
        
        return dp(0, 1)