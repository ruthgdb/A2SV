class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        queue = deque([(source, 0)])
        visitedRoutes = set()
        visitedBuses = set()
        
        for i, bus in enumerate(routes):
            for route in bus:
                graph[route].append(i)
                 
        while queue:
            curr, steps = queue.popleft()
            
            if curr == target:
                return steps
            
            for nei in graph[curr]:
                if nei in visitedBuses:
                    continue
                for route in routes[nei]:
                    if route not in visitedRoutes:
                        queue.append((route, steps + 1))
                        visitedRoutes.add(route)
                        
                    visitedBuses.add(nei)
             
        return -1