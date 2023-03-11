class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m 
  
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        parents = {}
        n = len(grid1)
        m = len(grid1[0])
        count = 0
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            isValid = True
            
            for x, y in DIR:
                nr = row + x
                nc = col + y
                
                if not self.inbound(nr, nc, n, m) or (nr, nc) in visited:
                    continue
                    
                if not grid1[nr][nc] and grid2[nr][nc]:
                    isValid = False
                
                if grid1[nr][nc] and grid2[nr][nc]:
                    visited.add((nr, nc))
                    if not dfs(nr, nc):
                        isValid = False
            
            return isValid
            
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid2[i][j] and grid1[i][j]:
                    visited.add((i, j))
                    if dfs(i, j):
                        count += 1
      
        return count