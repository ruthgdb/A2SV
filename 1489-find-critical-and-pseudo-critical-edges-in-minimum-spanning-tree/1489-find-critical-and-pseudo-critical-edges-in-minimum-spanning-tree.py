class UnionFind:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
            
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        
        if pu == pv: 
            return False
        
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        
        def find_mst_without_this_edge(edge_idx):
            union_find = UnionFind(n)
            ans = 0
            
            for i, (u, v, w, _) in enumerate(edges):
                if i == edge_idx:
                    continue
                if union_find.union(u, v):
                    ans += w
                    
            parent = union_find.find(0)
            return ans if all(union_find.find(i) == parent for i in range(n)) else inf
        
        def find_mst_with_this_edge(edge_idx):
            union_find = UnionFind(n)
            u0, v0, w0, _ = edges[edge_idx]
            ans = w0
            union_find.union(u0, v0)
            
            for i, (u, v, w, _) in enumerate(edges):
                if i == edge_idx:
                    continue
                if union_find.union(u, v):
                    ans += w
                    
            parent = union_find.find(0)
            return ans if all(union_find.find(i) == parent for i in range(n)) else inf
        
        base = find_mst_without_this_edge(-1)
        critical, pseudo_critical = set(), set()
        
        for i in range(len(edges)):
            excluded = find_mst_without_this_edge(i)
            if excluded > base:
                critical.add(edges[i][3])
            else:
                included = find_mst_with_this_edge(i)
                if included == base:
                    pseudo_critical.add(edges[i][3])
    
        return [critical, pseudo_critical]