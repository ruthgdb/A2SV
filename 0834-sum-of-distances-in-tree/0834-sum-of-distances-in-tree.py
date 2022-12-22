class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        result = [0] * n
        count = [1] * n
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        def dfs(node, parent):
            for neighbour in graph[node]:
                if neighbour != parent:
                    dfs(neighbour, node)
                    count[node] += count[neighbour]
                    result[node] += result[neighbour] + count[neighbour]
            
        def dfs2(node, parent): 
            for neighbour in graph[node]:
                if neighbour != parent:
                    result[neighbour] = result[node] - 2 * count[neighbour] + n
                    dfs2(neighbour, node)
        
        dfs(0, -1)
        dfs2(0, -1)
        return result