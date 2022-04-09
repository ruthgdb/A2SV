from collections import defaultdict

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = defaultdict(int)
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i >= n or j >= m:
                return float("inf")
            
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            
            if (i, j) in memo: 
                return memo[(i, j)]
            
            memo[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
            return memo[(i, j)]
                
        return dfs(0, 0)