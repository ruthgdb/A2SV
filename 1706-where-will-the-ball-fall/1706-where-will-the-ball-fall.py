class Solution:
    def is_inbound(self, col, m):
        return 0 <= col < m
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        balls = list(range(m))
        
        for i in range(n): 
            for j in range(m):
                curr_shift = balls[j]
                if curr_shift == -1:
                    continue
                idx = curr_shift + grid[i][curr_shift]
                if not self.is_inbound(idx, m) or grid[i][idx] == -grid[i][curr_shift]:
                    balls[j] = -1
                    continue
                balls[j] += grid[i][curr_shift]
        
        return balls