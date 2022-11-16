class Solution:
    def count_cells(self, board, row, col):
        count = 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        for dx, dy in DIR:
            nr = row + dx
            nc = col + dy
                    
            if self.inbound(nr, nc, len(board), len(board[0])) and board[nr][nc] % 2 == 1:
                count += 1
                
        return count
                
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive_cells = self.count_cells(board, i, j)

                if board[i][j] == 0:
                    if alive_cells == 3:
                        board[i][j] = 2
                else:
                    if alive_cells < 2 or alive_cells > 3:
                        board[i][j] = 3
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0