class Solution:
    def is_inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m
    
    def find(self, node, parents, rank):
        if parents[node] == node:
            return node
        
        parents[node] = self.find(parents[node], parents, rank)
        return parents[node]

    def union(self, u, v, parents, rank):
        first_parent = self.find(u, parents, rank)
        second_parent = self.find(v, parents, rank)
            
        if first_parent == second_parent: 
            return True

        rank1 = rank[first_parent]
        rank2 = rank[second_parent]
    
        if rank1 > rank2:
            parents[second_parent] = first_parent
            rank[first_parent] += rank2
        else: 
            parents[first_parent] = second_parent
            rank[second_parent] += rank1

        return False

        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rank = defaultdict(lambda: 1)
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
                        if self.union((i, j), (nr, nc), parents, rank):
                            return True
                        
        return False