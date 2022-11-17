class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        memo = {}
        
        def traverse(total):
            if total in memo:
                return memo[total]
            
            if total == 0:
                return 0
            
            if total < 0:
                return float("inf")
                
            mini = float("inf")
            
            for coin in coins:
                mini = min(mini, traverse(total - coin) + 1)
            
            memo[total] = mini
            return mini
            
        min_coins = traverse(amount)
        return min_coins if min_coins != float("inf") else -1