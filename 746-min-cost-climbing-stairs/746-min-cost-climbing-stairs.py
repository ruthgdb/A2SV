class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def minCost(i):           
            if i >= len(cost):
                return 0
            
            if i not in memo:
                memo[i] = min(minCost(i + 1), minCost(i + 2)) + cost[i]   
                
            return memo[i]
            
        return min(minCost(0), minCost(1))