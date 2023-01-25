class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        for n, nei in enumerate(edges):
            adj[n].append(nei)
        
        def bfs(src, dist_map):
            q = deque()
            q.append([src, 0])
            dist_map[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in dist_map:
                        q.append([nei, dist + 1])
                        dist_map[nei] = dist + 1
        
        node1_map = {} 
        node2_map = {}
        bfs(node1, node1_map)
        bfs(node2, node2_map)

        res = -1
        cur_dist = float("inf")
        for i in range(len(edges)):
            if i in node1_map and i in node2_map:
                dist = max(node1_map[i], node2_map[i])
                if dist < cur_dist:
                    res = i
                    cur_dist = dist
        
        return res