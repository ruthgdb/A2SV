class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        grid = [[1] * n] * m
        # grid[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                left = grid[i - 1][j] if i - 1 > 0 else 0
                up = grid[i][j - 1] if j - 1 > 0 else 0
                grid[i][j] = 1 + left + up
                
        return grid[-1][-1] + 1