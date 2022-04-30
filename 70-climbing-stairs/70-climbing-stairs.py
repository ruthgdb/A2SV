class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def stairs(x):
            if x < 3:
                return x
            
            if x not in memo.keys():
                memo[x] = stairs(x - 1) + stairs(x - 2)
            
            return memo[x]
        
        return stairs(n)