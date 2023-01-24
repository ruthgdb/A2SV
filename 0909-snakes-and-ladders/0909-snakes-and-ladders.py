class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]
        
        def cellToLoc(loc):
            r = (loc - 1) // n
            c = (loc - 1) % n
            if r % 2:
                c = n - c - 1
            return board[r][c]

        moves = 0
        location = deque([1])   # start
        visited = set([1])
        
        while location:
            for _ in range(len(location)):
                currLoc = location.popleft()
                if currLoc == n ** 2:
                    return moves
                
                for newLoc in range(currLoc + 1, min(currLoc + 6, n ** 2) + 1):
                    if newLoc not in visited:
                        visited.add(newLoc)
                        cellValue = cellToLoc(newLoc)
                        if cellValue == -1:
                            location.append(newLoc)

                        else:
                            location.append(cellValue)

            moves += 1

        return -1