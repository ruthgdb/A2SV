class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIRs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(image), len(image[0])
        inbound = lambda r, c: 0 <= r < m and 0 <= c < n
        start = image[sr][sc]
        
        def dfs(r, c):
            if image[r][c] != start:
                return
            
            image[r][c] = color
            
            for DIR in DIRs:
                nr, nc = r + DIR[0], c + DIR[1]
                
                if inbound(nr, nc):
                    dfs(nr, nc)
                       
        if start == color:
            return image
        
        dfs(sr, sc)
        return image