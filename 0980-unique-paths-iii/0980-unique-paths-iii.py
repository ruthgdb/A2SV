class Solution:
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        empty_cells = 1
        visited = set()
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(row, col, count):
            nonlocal result, empty_cells
            if grid[row][col] == 2:
                if count == empty_cells:
                    result += 1
                return 
                      
            for dx, dy in DIR:
                nr = dx + row
                nc = dy + col
                      
                if not self.is_inbound(nr, nc, n, m) or (nr, nc) in visited:
                    continue
                
                if grid[nr][nc] == -1:
                    continue
                    
                visited.add((nr, nc))
                backtrack(nr, nc, count + 1)
                visited.remove((nr, nc))

                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empty_cells += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    backtrack(i, j, 0)      
                    return result