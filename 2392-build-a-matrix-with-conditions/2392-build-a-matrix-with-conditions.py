class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        grid = [[0 for _ in range(k)] for _ in range(k)]
        rows = defaultdict(int)
        indegrees = [0] * k
        queue = deque()
        graph = defaultdict(list)
        visited = set()
        
        for first, second in rowConditions:
            graph[first - 1].append(second - 1)
            indegrees[second - 1] += 1
            
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
                
        i = 0
        
        while queue:
            curr_num = queue.popleft()
            
            if curr_num in visited:
                continue
                
            rows[curr_num] = i
            i += 1
            
            for next_num in graph[curr_num]:
                indegrees[next_num] -= 1
                
                if indegrees[next_num] == 0:
                    queue.append(next_num)
                    
        if not all(indegree == 0 for indegree in indegrees):
            return []
        
        visited.clear()
        graph.clear()
        
        for first, second in colConditions:
            graph[first - 1].append(second - 1)
            indegrees[second - 1] += 1
            
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
                
        j = 0
        
        while queue:
            curr_num = queue.popleft()
            
            if curr_num in visited:
                continue
                
            i = rows[curr_num]
            grid[i][j] = curr_num + 1
            j += 1
            
            for next_num in graph[curr_num]:
                indegrees[next_num] -= 1
                
                if indegrees[next_num] == 0:
                    queue.append(next_num)
                    
        if not all(indegree == 0 for indegree in indegrees):
            return []
        
        return grid