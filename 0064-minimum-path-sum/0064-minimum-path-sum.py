class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                left = dp[i][j - 1] if j > 0 else float("inf")
                top =  dp[i - 1][j] if i > 0 else float("inf")
                dp[i][j] = min(top, left) + grid[i][j]
                
        return dp[-1][-1]