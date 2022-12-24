class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        queue = deque([0])
        visited = set()
        changedEdges = 0
        
        for city1, city2 in connections:
            graph[city1].append((city2, 1))
            graph[city2].append((city1, 0))
        
        while queue:
            currCity = queue.popleft()

            if currCity in visited:
                continue
                
            visited.add(currCity)
            
            for neighbour, d in graph[currCity]:
                if neighbour not in visited:
                    changedEdges += d
                    queue.append(neighbour)
                             
        return changedEdges