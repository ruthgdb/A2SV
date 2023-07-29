class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        
        n = ceil(n / 25)
        dp = defaultdict(dict)

        @cache
        def dp(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            
            if i <= 0:
                return 1.0
            
            if j <= 0:
                return 0.0

            return (dp(i - 4, j) + dp(i - 3, j - 1) + dp(i - 2, j - 2) + dp(i - 1, j - 3)) / 4
        
        return dp(n, n)