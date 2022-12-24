class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        visited = set()
        
        def backtrack(i, j):
            visited.add((i, j))
            curr = 0
            
            for x, y in DIR:
                nr = x + i
                nc = y + j
                
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] > 0:
                    curr = max(curr, backtrack(nr, nc) + grid[nr][nc])
                  
            visited.remove((i, j))
            return curr
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    visited.clear()
                    maxGold = max(maxGold, backtrack(i, j) + grid[i][j])    
                    
        return maxGold