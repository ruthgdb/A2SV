class Solution:
    def inbound(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.m
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        closedIslands = 0
        
        def dfs(row, col):
            
            isClosed = True
            
            for x, y in dirs:
                nr = x + row
                nc = y + col
                
                if not self.inbound(nr, nc):
                    isClosed = False
                    continue
                
                if (nr, nc) not in visited and not grid[nr][nc]:
                    visited.add((nr, nc))
                    if not dfs(nr, nc):
                        isClosed = False
                    
            return isClosed
        
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) not in visited and not grid[i][j]:
                    visited.add((i, j))
                    if dfs(i, j):
                        closedIslands += 1
                        
        return closedIslands