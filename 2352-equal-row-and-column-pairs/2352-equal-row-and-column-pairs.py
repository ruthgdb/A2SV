class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = [[] for i in range(len(grid[0]))]
        count = 0
        
        for row in grid:
            currRow = '-'.join([str(i) for i in row])
            rows[currRow] += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cols[j].append(str(grid[i][j]))
                        
        for col in cols:
            currCol = '-'.join(col)
            count += rows[currCol]
            
        return count