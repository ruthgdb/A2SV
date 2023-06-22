class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 1 - bought
        # 0 - free
        
        @cache
        def dp(i, status):
            if i == len(prices):
                return 0
            
            notBuy = dp(i + 1, status)
            
            if status:
                buy = prices[i] + dp(i + 1, 0)
            else:
                buy = dp(i + 1, 1) - prices[i] - fee
            
            return max(buy, notBuy)
   
        return max(dp(0, 1) - prices[0] - fee, dp(0, 0))