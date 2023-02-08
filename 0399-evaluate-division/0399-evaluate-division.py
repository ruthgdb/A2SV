class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []
        
        def bfs(num1, num2):
            queue = deque([(num1, 1)])
            visited = set()
            
            while queue:
                curr, val = queue.popleft()
                visited.add(curr)
                
                if curr == num2:
                    return val
                
                for nei, nxtVal in graph[curr]:
                    if nei not in visited:
                        queue.append((nei, nxtVal * val))
                
            return -1
        
        for i, equation in enumerate(equations):
            num1, num2 = equation
            graph[num1].append((num2, values[i]))
            if values[i] != 0:
                graph[num2].append((num1, 1/values[i]))
        
        for query in queries:
            if query[0] in graph and query[1] in graph:
                res.append(bfs(*query))
            else:
                res.append(-1)
            
        return res