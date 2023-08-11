class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = []
        
        for i in coins:
            dp.append([0 for i in range(amount + 1)])
            
        for j in range(amount + 1):
            for i in range(len(coins)):
                if j == 0: 
                    dp[i][j] = 1
                else:
                    if j - coins[i] >= 0:
                        dp[i][j] = dp[i][j - coins[i]]
                    if i > 0: dp[i][j] += dp[i - 1][j]
                
        return dp[-1][-1]