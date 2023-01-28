class Solution:
    def __init__(self):
        self.DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.visited = set()
        
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def dfs(self, row, col, idx, board, word, n, m):
        if idx == len(word):
            return True
        
        if idx > len(word):
            return False
        
        found = False
        
        for dx, dy in self.DIR:
            nr = row + dx
            nc = col + dy
            
            if self.is_inbound(nr, nc, n, m) and board[nr][nc] == word[idx] and (nr, nc) not in self.visited:
                self.visited.add((nr, nc))
                found = found or self.dfs(nr, nc, idx + 1, board, word, n, m)
                self.visited.remove((nr, nc))
                
        return found
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    self.visited.add((i, j))
                    if self.dfs(i, j, 1, board, word, n, m):
                        return True
                    self.visited.remove((i, j))
                    
        return False