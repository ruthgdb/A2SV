class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        queue = deque([(0, 0)])
        n = len(grid)
        m = len(grid[0])
        DIR = [(0, 1, 'r'), (1, 0, 'd'), (-1, 0, 'u'), (0, -1, 'l')]
        roads = {1: [("l", 4), ("l", 6), ("l", 1), ("r", 3), ("r", 5), ("r", 1)],
                 2: [("u", 4), ("u", 2), ("u", 3), ("d", 6), ("d", 5), ("d", 2)],
                 3: [("l", 4), ("l", 6), ("l", 1), ("d", 6), ("d", 5), ("d", 2)],
                 4: [("r", 5), ("r", 3), ("r", 1), ("d", 6), ("d", 5), ("d", 2)],
                 5: [("u", 4), ("u", 3), ("u", 2), ("l", 4), ("l", 6), ("l", 1)],
                 6: [("u", 4), ("u", 3), ("u", 2), ("r", 5), ("r", 3), ("r", 1)]
                }
        
        while queue:
            row, col = queue.popleft()
            
            if (row, col) == (n - 1, m - 1):
                return True
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for x, y, d in DIR:
                nr = row + x
                nc = col + y
                
                if not self.inbound(nr, nc, n, m) or (nr, nc) in visited:
                    continue
                
                if (d, grid[nr][nc]) in roads[grid[row][col]]:
                    queue.append((nr, nc))
            
        return False