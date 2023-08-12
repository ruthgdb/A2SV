class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    top = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] += left + top
        
        return dp[-1][-1]