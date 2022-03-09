class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        visited = set()
        count = 0
        
        def dfs(row, col):
            visited.add((row,col))
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if inbound(newRow, newCol) and \
            grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
            
            
        start = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        
        return count