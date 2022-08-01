class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    left = obstacleGrid[i][j - 1] if j >= 1 else 0
                    up = obstacleGrid[i - 1][j] if i >= 1 else 0
                    obstacleGrid[i][j] = left + up
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] += 1
                    
        return obstacleGrid[-1][-1]