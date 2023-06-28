import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        heap = []
        visited = set()
        graph = defaultdict(list)
        
        for i, (node1, node2) in enumerate(edges):
            graph[node1].append((node2, i))
            graph[node2].append((node1, i))
        
        for node, i in graph[start]:
            heappush(heap, (-succProb[i], node, i))
                
        while heap:
            currProb, node, idx = heappop(heap)
            visited.add(node)
            
            if node == end:
                return -currProb
            
            for nei, i in graph[node]:
                if nei not in visited:
                    heappush(heap, (-(-currProb * succProb[i]), nei, i))
            
        return 0