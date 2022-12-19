class Solution:
    def bfs(self, graph, queue, visited, source, destination):
        while queue:
            currNode = queue.popleft()
            
            if currNode == destination:
                return True
            
            if currNode in visited:
                continue
                
            visited.add(currNode)
            
            for neighbour in graph[currNode]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        queue = deque([source])
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        return self.bfs(graph, queue, visited, source, destination)