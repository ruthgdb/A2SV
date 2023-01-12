class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [1] * n
        graph = defaultdict(list)
        
        def dfs(parent, node):
            total = 0
            count = defaultdict(int)
            
            for nei in graph[node]:
                if nei != parent:
                    curr = dfs(node, nei)
                    curr[labels[nei]] += 1
                    total += curr[labels[node]]
                    
                    for i in curr:
                        count[i] += curr[i]
            
            res[node] += total
            return count
                    
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
                
        dfs(-1, 0)
        return res