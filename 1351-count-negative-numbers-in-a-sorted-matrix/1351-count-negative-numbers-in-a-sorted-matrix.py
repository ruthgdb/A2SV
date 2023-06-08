class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row = 0
        col = m - 1
        count = 0

        while col >= 0 and row < n:
            if grid[row][col] < 0:
                count += n - row
                col -= 1
            else:
                row += 1

        return count