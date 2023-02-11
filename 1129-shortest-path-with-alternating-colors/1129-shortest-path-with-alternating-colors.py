class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)
        res, visited = [inf] * n, set()
        
        for node1, node2 in redEdges:
            red[node1].append(node2)
            
        for node1, node2 in blueEdges:
            blue[node1].append(node2)
            
        q = deque([(0, True, 0), (0, False, 0)])
        
        while q:
            val, color, l = q.popleft()
            if (val, color) in visited: continue
            res[val] = min(res[val], l)
            visited.add((val, color))
            
            if color:
                for node in red[val]:
                    q.append((node, not color, l + 1))
            else:
                for node in blue[val]:
                    q.append((node, not color, l + 1))
                
        for i in range(len(res)):
            if res[i] == inf: res[i] = -1
                
        return res