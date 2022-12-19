class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        # row, col, open, close
        n = len(grid)
        m = len(grid[0])
        DIR = [(0, 1), (1, 0)]
        
        if grid[0][0] == ')':
            return False
        
        @cache
        def dfs(row, col, opens, close):
            if (row, col) == (n - 1, m - 1):
                return opens == close
                        
            for x, y in DIR:
                nr = row + x
                nc = col + y
                
                if not self.inbound(nr, nc, n, m):
                    continue
                
                currOpen = opens
                currClose = close
                
                if grid[nr][nc] == '(':
                    currOpen += 1
                else:
                    currClose += 1
                    
                if currClose <= currOpen:
                    currPath = dfs(nr, nc, currOpen, currClose)
                    if currPath:
                        return True
                                        
            return False
   
        return dfs(0, 0, 1, 0)