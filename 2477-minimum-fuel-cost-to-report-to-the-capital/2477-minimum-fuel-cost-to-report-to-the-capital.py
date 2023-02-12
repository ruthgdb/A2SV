class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
            
        fuel = 0
        
        def dfs(v, parent):
            nonlocal seats, fuel
            people = 1
            for ch in graph[v]:
                if ch != parent:
                    people += dfs(ch, v)
            if v != 0:
                fuel += math.ceil(people / seats)
                
            return people
        
        dfs(0, -1)
        return fuel