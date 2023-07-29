class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        visited_cols = set()
        visited_left_diagonals = set()
        visited_right_diagonals = set()
        
        def backtrack(i):
            if i == n:
                res.append(["".join(x) for x in grid])
                
            for j in range(n):
                if j not in visited_cols and \
                i - j not in visited_left_diagonals and \
                i + j not in visited_right_diagonals:
                    visited_cols.add(j)
                    visited_left_diagonals.add(i - j)
                    visited_right_diagonals.add(i + j)
                    
                    grid[i][j] = 'Q'
                    
                    backtrack(i + 1)
                    visited_cols.remove(j)
                    visited_left_diagonals.remove(i - j)
                    visited_right_diagonals.remove(i + j)
                    grid[i][j] = '.'
                        
        backtrack(0)
        return res