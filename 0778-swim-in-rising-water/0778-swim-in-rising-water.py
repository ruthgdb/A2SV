class Solution:
    def check_time(self, time, grid):
        if grid[0][0] > time:
            return False
        
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)
        inbound = lambda x, y: 0 <= x < n and 0 <= y < n
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            row, col = queue.popleft()
            
            if (row, col) == (n - 1, n - 1):
                return True
            
            for x, y in DIR:
                nr = row + x
                nc = col + y
                
                if (nr, nc) in visited or not inbound(nr, nc):
                    continue
                
                if grid[nr][nc] <= time:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
        return False
        
    def swimInWater(self, grid: List[List[int]]) -> int:
        left = 0
        right = len(grid) ** 2 - 1
        best = len(grid) ** 2 - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.check_time(mid, grid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best