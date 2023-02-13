class Solution:
    def inbound(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])
        n = len(grid)
        visited = set()
        Dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        shortestPath = float("inf")
        
        while queue:
            row, col, dist = queue.popleft()
            
            if (row, col) == (n - 1, n - 1):
                shortestPath = min(shortestPath, dist)
                
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for x, y in Dir:
                nr = x + row
                nc = y + col
                
                if self.inbound(nr, nc, n) and (nr, nc) not in visited and not grid[nr][nc]:
                    queue.append((nr, nc, dist + 1))
            
        return shortestPath if shortestPath!= float("inf") else -1