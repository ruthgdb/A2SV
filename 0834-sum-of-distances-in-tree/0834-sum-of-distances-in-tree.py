class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        result = [0] * n
        count = [1] * n
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        @cache
        def dfs(parent, node):
            dist = 0
            count = 1
            
            for nei in graph[node]:
                if nei != parent:
                    d, c = dfs(node, nei)
                    count += c
                    dist += d + c
            
            return (dist, count)
            
        for i in range(n):
            dist, count = dfs(-1, i)
            result[i] = dist
            
        return result