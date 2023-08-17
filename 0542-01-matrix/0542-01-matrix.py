import heapq

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        heap = []
        res = [[0 for _ in range(m)] for _ in range(n)]
        visited = set()
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    heappush(heap, (0, i, j))
                    
        while heap:
            dist, i, j = heappop(heap)
            
            if (i, j) in visited:
                continue
                
            res[i][j] = dist
            visited.add((i, j))
            
            for x, y in DIR:
                nr = x + i
                nc = y + j
                
                if not inbound(nr, nc) or (nr, nc) in visited:
                    continue
                    
                heappush(heap, (dist + 1, nr, nc))
                
        return res