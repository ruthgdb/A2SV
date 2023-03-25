class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        pairs = 0
        nodes = 0
        
        def dfs(i):
            count = 1
            
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    count += dfs(j)

            return count
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
       
        for i in range(n):
            if i not in visited:
                visited.add(i)
                count = dfs(i)
                pairs += nodes * count
                nodes += count
                
        return pairs
    