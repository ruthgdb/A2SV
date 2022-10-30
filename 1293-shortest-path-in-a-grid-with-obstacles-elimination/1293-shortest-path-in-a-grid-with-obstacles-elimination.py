class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        DIRs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([((0, 0), 0, 0)])
        visited = set()
           
        while queue:
            curr_cell, obstacles, dist = queue.popleft()
            row, col = curr_cell
            
            if curr_cell == (n - 1, m - 1):
                return dist
            
            for x, y in DIRs:
                nr = row + x
                nc = col + y
                if not inbound(nr, nc):
                    continue
                left = obstacles + grid[nr][nc]
                
                if (nr, nc, left) not in visited and left <= k:
                    queue.append(((nr, nc), left, dist + 1))
                    visited.add((nr, nc, left))
                    
        return -1