class Solution:
    def maxIncreasingCells(self, grid: List[List[int]]) -> int:
        '''
        rows
        0: 1 (1), 3 (0), 6 (2) 
        1: -9 (0), 5 (1), 7 (2)
        
        cols
        0: -9 (1), 3 (0)
        1: 1 (0), 5 (1)
        2: 6 (0), 7 (1)
        
        sorted version
        -9 (1, 0), 1 (0, 1), 3 (0, 0), 5 (1, 1), 6 (0, 2), 7 (1, 2)
        
        
        [7,  6,  3]
        [-7,-5,  6]
        [-7, 0, -4]
        [6,  6,  0]
        [-8, 6,  0]
        
        '''
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        sorted_cells = sorted([(grid[i][j], i, j) for j in range(m) for i in range(n)] )
        rows = defaultdict(list)
        cols = defaultdict(list)
        max_len = 1
        
        for i in range(n):
            for j in range(m):
                rows[i].append((grid[i][j], j))
                cols[j].append((grid[i][j], i))
                
        for i in rows:
            rows[i].sort()
            
        for j in cols:
            cols[j].sort()
            
        def find_max_row(row_idx, i):
            max_val = dp[i][rows[i][row_idx][1]] if row_idx < len(rows[i]) else 0
            
            for idx in range(row_idx + 1, len(rows[i])):
                if rows[i][idx][0] != rows[i][row_idx][0]:
                    break
                    
                max_val = max(max_val, dp[i][rows[i][idx][1]])
                    
            return max_val
            
        def find_max_col(col_idx, j):
            max_val = dp[cols[j][col_idx][1]][j] if col_idx < len(cols[j]) else 0
            
            for idx in range(col_idx + 1, len(cols[j])):
                if cols[j][idx][0] != cols[j][col_idx][0]:
                    break
                    
                max_val = max(max_val, dp[cols[j][idx][1]][j])
                    
            return max_val
            
        for idx in range(len(sorted_cells) - 1, -1, -1):
            val, i, j = sorted_cells[idx]
            row_max_idx = bisect.bisect_left(rows[i], (val, float("inf")))
            col_max_idx = bisect.bisect_left(cols[j], (val, float("inf")))
            row_max = find_max_row(row_max_idx, i)
            col_max = find_max_col(col_max_idx, j)
            dp[i][j] = max(row_max, col_max) + 1
            max_len = max(max_len, dp[i][j])
            
        return max_len