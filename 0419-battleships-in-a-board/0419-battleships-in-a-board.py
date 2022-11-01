class Solution:
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        visited = set()
        count = 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def traverse(i, j):
            for dx, dy in DIR:
                nr = dx + i
                nc = dy + j

                if self.is_inbound(nr, nc, n, m) and (nr, nc) not in visited and board[nr][nc] == 'X':
                    visited.add((nr, nc))
                    traverse(nr, nc)
                    
            return

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and board[i][j] == 'X':
                    traverse(i, j)
                    count += 1

        return count
