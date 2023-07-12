class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegrees = [0] * len(graph)
        relations = defaultdict(list)
        safe_nodes = []
        queue = deque()
        visited = set()
        
        for i, adj_nodes in enumerate(graph):
            for node in adj_nodes:
                relations[node].append(i)
                indegrees[i] += 1
                
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                
                queue.append(i)
                
        while queue:
            curr_node = queue.popleft()
            
            if curr_node in visited:
                continue
                
            safe_nodes.append(curr_node)
            visited.add(curr_node)
            
            for adj_nodes in relations[curr_node]:
                indegrees[adj_nodes] -= 1
                
                if indegrees[adj_nodes] == 0:
                    queue.append(adj_nodes)
                
        return sorted(safe_nodes)