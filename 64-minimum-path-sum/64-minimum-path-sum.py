class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = dict()
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            if (i, j) in memo.keys():
                return memo[(i, j)]
            
            if i == n - 1 and j == m - 1:
                memo[(i, j)] = grid[i][j]
                return memo[(i, j)]
            if i == n - 1:
                memo[(i, j)] = dfs(i, j + 1) + grid[i][j]
                return memo[(i, j)]
            if j == m - 1:
                memo[(i, j)] = dfs(i + 1, j) + grid[i][j]
                return memo[(i, j)]
            
            memo[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
            return memo[(i, j)]
        
        if n == m == 1:
            return grid[0][0]
        if n == 1:
            return grid[0][0] + dfs(0, 1)
        if m == 1:
            return grid[0][0] + dfs(1, 0)
                    
        return grid[0][0] + min(dfs(0, 1), dfs(1, 0))