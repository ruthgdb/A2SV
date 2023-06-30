class Solution:
    def inbound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:    
        visited = set() # i, j, keyBit
        minDist = float("inf")
        keys = 0
        queue = deque()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0)) # i, j, dist, keyBit
                if grid[i][j] in ('a', 'b', 'c', 'd', 'e', 'f'):
                    keys += 1
                    
        fullKeysBit = (1 << keys) - 1
                    
        while queue:
            i, j, currDist, keyBit = queue.popleft()
            
            if keyBit == fullKeysBit:
                minDist = min(minDist, currDist)
            
            if (i, j, keyBit) in visited:
                continue
                
            visited.add((i, j, keyBit))
            
            for x, y in dirs:
                nr = i + x
                nc = j + y
                
                if not self.inbound(nr, nc, grid) or (nr, nc, keyBit) in visited or \
                grid[nr][nc] == '#':
                    continue
                    
                if grid[nr][nc].isalpha():
                    if grid[nr][nc].isupper():
                        num = ord(grid[nr][nc]) - 65
                        shiftBit = 1 << num
                        if keyBit & shiftBit != 0:
                            queue.append((nr, nc, currDist + 1, keyBit))
                    else:
                        num = ord(grid[nr][nc]) - 97
                        shiftBit = 1 << num
                        key = keyBit | shiftBit
                        queue.append((nr, nc, currDist + 1, key))
                else:
                    queue.append((nr, nc, currDist + 1, keyBit))
            
        return minDist if minDist != float("inf") else -1