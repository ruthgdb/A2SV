class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        n = len(grid)
        m = len(grid[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        count = 0
        
        def dfs(row, col):
            visited.add((row, col))
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if (newRow, newCol) not in visited and inbound(newRow, newCol) \
                and grid[newRow][newCol] == 1:
                    dfs(newRow, newCol)
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1)\
                and (i,j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == 1:
                    count += 1
                    
        return count