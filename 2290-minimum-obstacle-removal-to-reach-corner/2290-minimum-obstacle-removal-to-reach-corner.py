class Solution:
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        heap = [(0, 0, 0)]
        DIRs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[-1] * m for _ in range(n)]
        
        while heap:
            blocks, row, col = heapq.heappop(heap)
            visited[row][col] = 1
            
            if (row, col) == (n - 1, m - 1):
                return blocks
            
            for dx, dy in DIRs:
                nr = dx + row
                nc = dy + col
                
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                    visited[nr][nc] = 1
                    heapq.heappush(heap, (blocks + grid[nr][nc], nr, nc))