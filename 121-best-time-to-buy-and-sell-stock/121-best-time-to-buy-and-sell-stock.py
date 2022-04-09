class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0] * len(prices)
        minimum = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profits[i] = prices[i] - minimum
                
        return max(profits)