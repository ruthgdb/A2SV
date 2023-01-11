class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        def dfs(root, parent):
            total = 0
            
            for nei in graph[root]:
                if nei != parent:
                    total += dfs(nei, root)
            
            if total == 0:
                return hasApple[root] if root != 0 else total
                            
            return total + 1 if root != 0 else total
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        return dfs(0, -1) * 2