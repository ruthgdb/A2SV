class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        
        def tribonacci(x):            
            if x not in memo.keys():
                memo[x] = tribonacci(x - 3) + tribonacci(x - 2) + tribonacci(x - 1)
                
            return memo[x]
                
        return tribonacci(n)