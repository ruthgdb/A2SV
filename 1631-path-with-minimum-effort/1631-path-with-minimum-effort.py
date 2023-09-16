class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def can_reach_end(self, mid, grid):
        n = len(grid)
        m = len(grid[0])
        queue = deque([(0, 0)])
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        
        while queue:
            row, col = queue.popleft()
            
            if (row, col) == (n - 1, m - 1):
                return True
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for x, y in DIR:
                nr = x + row
                nc = y + col
                
                if not self.inbound(nr, nc, n, m) or (nr, nc) in visited:
                    continue
                    
                if abs(grid[nr][nc] - grid[row][col]) <= mid:
                    queue.append((nr, nc))
            
        return False
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left = 0
        right = max([j for i in heights for j in i])
        best = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.can_reach_end(mid, heights):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best