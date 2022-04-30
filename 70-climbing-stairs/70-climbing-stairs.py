class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        '''
        4:5
        5:8
        6:13   1 2 3 5 8 
        7:21
        8:24
        '''
    
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[-1]