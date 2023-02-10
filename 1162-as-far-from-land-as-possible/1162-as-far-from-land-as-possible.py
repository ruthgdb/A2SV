class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        nearestLand = float("-inf")
        
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    up = dp[i - 1][j] if i > 0 else float("inf")
                    left = dp[i][j - 1] if j > 0 else float("inf")
                    dp[i][j] = min(up + 1, left + 1)      
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down = dp[i + 1][j] + 1 if i < n - 1 else float("inf")
                right = dp[i][j + 1] + 1 if j < n - 1 else float("inf")
                dp[i][j] = min(down, right, dp[i][j])
                nearestLand = max(nearestLand, dp[i][j])
             
        return nearestLand if nearestLand != 0 and nearestLand != float("inf") else -1