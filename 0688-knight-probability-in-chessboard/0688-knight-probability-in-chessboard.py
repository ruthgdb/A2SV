class Solution:
    def inbound(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        DIR = [(1, -2), (2, -1), (2, 1), (1, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2)]
        
        @cache
        def dfs(i, j, k):
            if k == 0:
                return 1
            
            count = 0
            
            for x, y in DIR:
                nr = x + i
                nc = y + j
                
                if not self.inbound(nr, nc, n):
                    continue
                    
                count += dfs(nr, nc, k - 1)
                
            return count / 8
        
        return dfs(row, column, k)