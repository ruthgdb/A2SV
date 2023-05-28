class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        memo = {}
        
        def dp(i, j, cuts):
            if not cuts or j <= i:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            cost = j - i
            minCost = float("inf")
            
            for k, cut in enumerate(cuts):
                left = dp(i, cut, cuts[:k])
                right = dp(cut, j, cuts[k + 1:])
                minCost = min(minCost, left + right)
                
            cost += minCost
            memo[(i, j)] = cost
            return cost
        
        return dp(0, n, cuts)