class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        @lru_cache(None)
        def traverse(total):
            if total == amount:
                return 0
            
            if total > amount:
                return float("inf")
                
            mini = float("inf")
            
            for coin in coins:
                mini = min(mini, traverse(total + coin))
            
            return mini + 1
            
        min_coins = traverse(0)
        return min_coins if min_coins != float("inf") else -1