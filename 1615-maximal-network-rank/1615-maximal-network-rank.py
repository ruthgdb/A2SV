class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        max_network = 0
        indegrees = [0] * n
        
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
            indegrees[city1] += 1
            indegrees[city2] += 1
            
        for i in range(n):
            for j in range(i + 1, n):
                if i in graph[j]:
                    max_network = max(max_network, indegrees[i] + indegrees[j] - 1)
                else:
                    max_network = max(max_network, indegrees[i] + indegrees[j])
                    
        return max_network