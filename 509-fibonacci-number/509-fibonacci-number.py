class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def search(x):
            if x < 2:
                return x
            
            if x not in memo.keys():            
                memo[x] = self.fib(x - 1) + self.fib(x - 2)
                
            return memo[x]
        
        return search(n)