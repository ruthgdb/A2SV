class Solution:
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def find(self, node, parents):
        if parents[node] == node:
            return node
        
        parents[node] = self.find(parents[node], parents)
        return parents[node]

    def union(self, u, v, parents):
        first_parent = self.find(u, parents)
        second_parent = self.find(v, parents)
            
        if first_parent == second_parent: 
            return True

        parents[second_parent] = first_parent

        return False
        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        parents = {}
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parents[(i, j)] = (i, j)
                
        
        for i in range(n):
            for j in range(m):
                letter = grid[i][j]
                visited.add((i, j))
                
                for dx, dy in DIR:
                    nr = dx + i
                    nc = dy + j
                    
                    if not self.is_inbound(nr, nc, n, m) or (nr, nc) in visited:
                        continue
                        
                    if grid[nr][nc] == letter:
                        if self.union((i, j), (nr, nc), parents):
                            return True
                        
        return False