class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @cache
        def dp(i):
            if i == len(stoneValue):
                return 0
            
            result = stoneValue[i] - dp(i + 1)
            
            if i + 2 <= len(stoneValue):
                result = max(result, stoneValue[i] + stoneValue[i + 1] - dp(i + 2))
                
            if i + 3 <= len(stoneValue):
                result = max(result, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp(i + 3))
                
            return result

        res = dp(0)
        
        if res > 0:
            return "Alice"
        if res < 0:
            return "Bob"
        
        return "Tie"