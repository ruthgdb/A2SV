class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        
        def dfs(row):
            for col in range(len(isConnected[row])):
                if col not in visited and isConnected[row][col] == 1:
                    visited.add(col)
                    dfs(col)
            
            
        for row in range(len(isConnected)):
            if row not in visited:
                count += 1
                visited.add(row)
                dfs(row)
        
        return count