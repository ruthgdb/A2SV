class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid)
        
        def dfs(i, j):
            grid[i][j] = "1"
            visited.add((i, j))
                
            for x, y in DIR:
                nr = x + i
                nc = y + j
                
                if not inbound(nr, nc):
                    continue
                    
                if grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    
                if (nr, nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        found = False
        
        for i in range(len(grid)):
            if found:
                break
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        queue = deque()
        level = 1
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == -1:
                    queue.append((i, j))
        
        while queue:
            l = len(queue)
            
            for _ in range(l):
                row, col = queue.popleft()
                if (row, col) in visited:
                    continue
                    
                visited.add((row, col))
                
                for x, y in DIR:
                    nr = x + row
                    nc = y + col

                    if not inbound(nr, nc) or (nr, nc) in visited:
                        continue
                    
                    if grid[nr][nc] == 1:
                        return level
                    
                    if grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        
            level += 1

