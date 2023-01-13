class Solution:
    def find(self, node, parents):
        if parents[node] == node:
            return node
        
        parents[node] = self.find(parents[node], parents)
        return parents[node]
        
    def union(self, u, v, dist, parents, rank):
        pu = self.find(u, parents)
        pv = self.find(v, parents)
        
        if pu != pv:
            parents[pu] = pv
            
        rank[pv] = min(rank[pv], rank[pu], dist)
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rank = [float("inf")] * n
        parents = [i for i in range(n)]
        
        for city1, city2, dist in roads:
            self.union(city1 - 1, city2 - 1, dist, parents, rank)
           
        for i in range(n):
            self.find(i, parents)
        
        return rank[self.find(0, parents)]