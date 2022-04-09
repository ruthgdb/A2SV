class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i != 0 or j != 0:
                    left = grid[i][j - 1] if j - 1 >= 0 else float("inf")
                    up = grid[i - 1][j] if i - 1 >= 0 else float("inf")
                    grid[i][j] += min(left, up)
                    
        return grid[-1][-1]