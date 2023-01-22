class Solution:
    def findBox(self, i, j):
        r = i // 3
        c = j // 3
        return( r * 3) + c
            
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res = [[] for _ in range(9)]
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[self.findBox(i, j)].add(board[i][j])

        def backtrack(i, j):
            nonlocal res
            if i == 8 and j == 8:
                if board[i][j] == '.':
                    for k in range(1, 10):
                        b = self.findBox(i, j)
                        k = str(k)

                        if k not in rows[i] and k not in cols[j] and k not in box[b]:
                            board[i][j] = k
                            break
                        
                for x in range(9):
                    res[x] = board[x][:]
                    
                return
                   
            if board[i][j] == '.':
                for k in range(1, 10):
                    b = self.findBox(i, j)
                    k = str(k)
                    
                    if k not in rows[i] and k not in cols[j] and k not in box[b]:
                        
                        rows[i].add(k)
                        cols[j].add(k)
                        box[b].add(k)

                        board[i][j] = k

                        if j + 1 < 9:
                            backtrack(i, j + 1)
                        elif i + 1 < 9:
                            backtrack(i + 1, 0)
                            
                        board[i][j] = '.'

                        rows[i].remove(k)
                        cols[j].remove(k)
                        box[b].remove(k)

            else:
                if j + 1 < 9:
                    backtrack(i, j + 1)
                elif i + 1 < 9:
                    backtrack(i + 1, 0)

        backtrack(0, 0)
        
        for i in range(9):
            for j in range(9):
                board[i][j] = res[i][j]