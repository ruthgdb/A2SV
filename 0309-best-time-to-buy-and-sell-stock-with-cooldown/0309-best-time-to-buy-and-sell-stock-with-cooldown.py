class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 - sell
        # 1 - buy
        # 2 - cooldown
        
        @cache
        def dp(i, status):
            if i == len(prices):
                return 0 if status != 1 else float("-inf")
            
            buy = cooldown = 0
            notBuy = dp(i + 1, status)
            
            if status == 0:
                buy = dp(i + 1, 1) - prices[i]
            elif status == 1:
                buy = prices[i] + dp(i + 1, 2) 
            else:
                cooldown = dp(i + 1, 0)
             
            return max(buy, cooldown, notBuy)
          
        return max(dp(0, 0), 0)