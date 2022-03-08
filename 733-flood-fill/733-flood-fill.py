class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]: 
        def dfs(row, col):
            image[row][col] = newColor
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]

                if inbound(newRow, newCol) and image[newRow][newCol] == start:
                    dfs(newRow, newCol)
        
        start = image[sr][sc]
        if start == newColor:
            return image
        
        image[sr][sc] = newColor
        n = len(image)
        m = len(image[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        dfs(sr, sc)
        return image