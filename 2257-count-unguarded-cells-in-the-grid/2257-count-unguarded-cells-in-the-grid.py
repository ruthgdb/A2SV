class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for i in range(m)]
        res = 0
        
        for i, j in walls:
            grid[i][j] = -1
            
        for i, j in guards:
            grid[i][j] = 1
            
        for i, j in guards:
            for bw in range(i - 1, -1, -1):
                if grid[bw][j] == -1 or grid[bw][j] == 1:
                    break
                grid[bw][j] = 2
                
            for fw in range(i + 1, m):
                if grid[fw][j] == -1 or grid[fw][j] == 1:
                    break
                grid[fw][j] = 2

            for uw in range(j - 1, -1, -1):
                if grid[i][uw] == -1 or grid[i][uw] == 1:
                    break
                grid[i][uw] = 2
                
            for dw in range(j + 1, n):
                if grid[i][dw] == -1 or grid[i][dw] == 1:
                    break
                grid[i][dw] = 2
            
        for i in range(m):
            res += grid[i].count(0)
            
        return res