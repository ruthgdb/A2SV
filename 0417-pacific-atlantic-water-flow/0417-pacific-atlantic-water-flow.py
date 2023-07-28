class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # set of cells that can flow to the pacific and atlantics
        pacifics = set()
        atlantics = set()
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        inbound = lambda x, y: 0 <= x < len(heights) and 0 <= y < len(heights[0])
        res = []
        
        # add cells to pacific set if they can flow to pacific
        def check_pacifics():
            queue = deque()
            visited = set()
            
            # add edge cells
            for j in range(len(heights[0])):
                queue.append((0, j))
                visited.add((0, j))
                
            for i in range(len(heights)):
                queue.append((i, 0))
                visited.add((i, 0))
                
            while queue:
                row, col = queue.popleft()
                pacifics.add((row, col))
                
                for x, y in DIR:
                    nr = x + row
                    nc = y + col
                    
                    if (nr, nc) in visited or not inbound(nr, nc):
                        continue
                      
                    if heights[row][col] <= heights[nr][nc]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                
            
        # add cells to atlantics set if they can flow to atlantic
        def check_atlantics():
            queue = deque()
            visited = set()
            
            # add edge cells
            for j in range(len(heights[0])):
                queue.append((len(heights) - 1, j))
                visited.add((len(heights) - 1, j))
                
            for i in range(len(heights)):
                queue.append((i, len(heights[0]) - 1))
                visited.add((i, len(heights[0]) - 1))
                
            while queue:
                row, col = queue.popleft()
                atlantics.add((row, col))
                
                for x, y in DIR:
                    nr = x + row
                    nc = y + col
                    
                    if (nr, nc) in visited or not inbound(nr, nc):
                        continue
                      
                    if heights[row][col] <= heights[nr][nc]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        check_pacifics()
        check_atlantics()
        
        #check if each cell is in pacific and atlantic set
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacifics and (i, j) in atlantics:
                    res.append([i, j])
                    
        return res