class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        queue = deque()
        
        def bfs(row):
            queue.append(row) 
            
            while queue:
                temp = queue.popleft()
                
                for col in range(len(isConnected[temp])):
                    if col not in visited and isConnected[temp][col] == 1:
                        visited.add(col)
                        bfs(col)
            
            
        for row in range(len(isConnected)):
            if row not in visited:
                count += 1
                queue.append(row)
                visited.add(row)
                bfs(row)
        
        return count