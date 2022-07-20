class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        DIRs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        def dfs(r, c):
            visited.add((r, c))
            
            for DIR in DIRs:
                nr = r + DIR[0]
                nc = c + DIR[1]
                
                if inbound(nr, nc) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    dfs(nr, nc)
            
            
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count
        