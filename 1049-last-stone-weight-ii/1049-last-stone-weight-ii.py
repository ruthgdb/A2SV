class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        @cache    
        def dp(i, sum1, sum2):
            if i == len(stones):
                return abs(sum1 - sum2) if sum1 != 0 and sum2 != 0 else float("inf")
                    
            firstWeight = dp(i + 1, sum1 + stones[i], sum2)
            secondWeight = dp(i + 1, sum1, sum2 + stones[i])
            return min(firstWeight, secondWeight)
            
        return dp(0, 0, 0)