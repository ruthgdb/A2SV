class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        queue = deque([click])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        
        while queue:
            row, col = queue.popleft()
            
            if board[row][col] != 'E':
                continue
         
            count = 0
            
            for x, y in DIR:
                nr = row + x
                nc = col + y
                
                if self.inbound(nr, nc, n, m) and board[nr][nc] == 'M':
                    count += 1
        
            if count == 0:
                for x, y in DIR:
                    nr = row + x
                    nc = col + y

                    if self.inbound(nr, nc, n, m) and board[nr][nc] == 'E':
                        queue.append([nr, nc])   
                    
                board[row][col] = 'B'
            else:
                board[row][col] = str(count)
                
        return board