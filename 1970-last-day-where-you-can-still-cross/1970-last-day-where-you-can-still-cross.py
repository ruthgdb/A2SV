class Solution:
    def __init__(self):
        self.cells = []
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.row = 0
        self.col = 0
        
    def inbound(self, i, j):
        return 0 <= i < self.row and 0 <= j < self.col
    
    def checkValidPath(self, mid):
        grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
        queue = deque()
        visited = set()
        
        for i in range(mid):
            row, col = self.cells[i]
            grid[row - 1][col - 1] = 1
                
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                queue.append((0, i))
                
        while queue:
            currRow, currCol = queue.popleft()
            
            if currRow == self.row - 1:
                return True
            
            if (currRow, currCol) in visited:
                continue
                
            visited.add((currRow, currCol))
            
            for dx, dy in self.dirs:
                nr = currRow + dx
                nc = currCol + dy
                
                if not self.inbound(nr, nc) or (nr, nc) in visited or grid[nr][nc] == 1:
                    continue
                    
                queue.append((nr, nc))
                
        return False
        
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.cells = cells
        self.row = row
        self.col = col
        left = 0
        right = row * col - 1
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.checkValidPath(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return best