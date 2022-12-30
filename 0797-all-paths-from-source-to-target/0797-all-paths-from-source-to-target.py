class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        queue = deque([(0, [])])
        
        while queue:
            node, path = queue.popleft()
            
            if node == len(graph) - 1:
                paths.append(path + [node])
               
            for nei in graph[node]:
                queue.append((nei, path + [node]))
                
        return paths