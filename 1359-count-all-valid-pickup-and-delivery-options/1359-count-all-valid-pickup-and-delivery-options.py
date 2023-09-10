class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(remaining, chosen, delivering, i):
            if chosen == n and i == n:
                return 1
            
            first, second = 0, 0
            
            if remaining > 0:
                first = remaining * dp(remaining - 1, chosen + 1, delivering + 1, i)
            
            if delivering > 0:
                second = delivering * dp(remaining, chosen, delivering - 1, i + 1)
            
            return first + second 
        
        return dp(n, 0, 0, 0) % MOD