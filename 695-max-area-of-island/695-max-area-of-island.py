class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.count = 0
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        visited = set()
        
        def dfs(row, col):
            self.count += 1
            visited.add((row,col))
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if inbound(newRow, newCol) and \
            grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == 1:
                    self.count = 0
                    dfs(row, col)
                    self.maxArea = max(self.maxArea, self.count)
        
        return self.maxArea