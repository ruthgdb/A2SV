class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions, queue = [[0, 1], [0, -1], [1, 0], [-1, 0]], deque()
        numRows, numCols, row, col = len(grid), len(grid[0]), 0, 0
        
        def paint(row, col):
            nonlocal grid, queue, numRows, numCols
            if min(row, col) >= 0 and max(row, col) < numRows and grid[row][col] == 1:
                grid[row][col] = 2
                queue.append((row, col))
                for direction in directions:
                    paint(row + direction[0], col + direction[1])
        
        while row < numRows and len(queue) == 0:
            col = 0
            while col < numCols and len(queue) == 0:
                paint(row, col)
                col += 1
            row += 1
            
        while queue:
            queue1 = deque()
            for row, col in queue:
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if min(newRow, newCol) >= 0 and max(newRow, newCol) < numRows:
                        if grid[newRow][newCol] == 1:
                            return grid[row][col] - 2
                        if grid[newRow][newCol] == 0:
                            grid[newRow][newCol] = grid[row][col] + 1
                            queue1.append((newRow, newCol))
                            
            queue, queue1 = queue1, queue
        return 0